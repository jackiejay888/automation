# -*- coding: utf-8 -*-
'''
Created on 2020/07/09

@author: ZL Chen
@title: The Wireless LAN should be worked after the airplane mode by android 10.0 is switch on/off.
'''

import os
import sys
import time
import subprocess
from subprocess import check_output


class airplane_wlan_single(object):

    global sum_pass
    global sum_fail
    sum_pass = 0
    sum_fail = 0

    def kill(self, filename):
        os.system('killall ' + filename)

    def kill_extension_file(self, filename_extension):
        os.system('rm -rf *.' + filename_extension)

    # ping the google servier by adb shell command
    def adb_command_set(self, value):
        self._adb_shell(value)

    # reponse messgae by adb shell command
    def adb_response_get(self, value):
        global sum_pass
        global sum_fail
        if '100% packet loss' in str(stdout):
            self._get_value(len(lines))
            sum_fail += 1
            os.system('echo The connection is Failed.(FAIL) >> ping_server.log')
            print('The connection is Failed.(FAIL)')
        elif value in str(stdout):
            self._get_value(len(lines))
            sum_pass += 1
            os.system('echo The connection is Passed.(PASS) >> ping_server.log')
            print('The connection is Passed.(PASS)')
        elif '25% packet loss' in str(stdout):
            self._get_value(len(lines))
            sum_pass += 1
            os.system('echo The connection is Passed.(PASS) >> ping_server.log')
            print('The connection is Passed.(PASS)')
        elif '50% packet loss' in str(stdout):
            self._get_value(len(lines))
            sum_pass += 1
            os.system('echo The connection is Passed.(PASS) >> ping_server.log')
            print('The connection is Passed.(PASS)')
        elif '75% packet loss' in str(stdout):
            self._get_value(len(lines))
            sum_pass += 1
            os.system('echo The connection is Passed.(PASS) >> ping_server.log')
            print('The connection is Passed.(PASS)')
        else:
            self._get_value(len(lines))
            sum_fail += 1
            os.system('echo The connection is Failed.(FAIL) >> ping_server.log')
            print('The connection is Failed.(FAIL)')

    def _get_value(self, round_times):
        try:
            for get in range(round_times):
                if get:
                    # echo = str(lines[get]).split('b\'')[1]
                    # os.system('echo ' + echo + ' >> ping_server.log')
                    os.system('echo ' + str(lines[get]) + ' >> ping_server.log')
        except:
            raise Exception('Cannot get the response message.')

    def _adb_shell(self, shell_cmds):
        global stdout
        global lines
        try:
            shell_cmds = shell_cmds + '; echo $?'
            cmds = ['adb', 'shell', shell_cmds]
            stdout = subprocess.Popen(
                cmds, stdout=subprocess.PIPE).communicate()[0].rstrip()
            lines = stdout.splitlines()
            # print(stdout)
            # os.system('echo stdout: ' + str(stdout) + ' >> ping_server.log')
            # print(lines)
            # os.system('echo lines: ' + str(lines) + ' >> ping_server.log')
        except:
            raise Exception('The adb shell is failed.')

    # launch the airplane mode
    def start_airplane(self):
        try:
            self._adb_shell('settings put global airplane_mode_on 1')
            self._adb_shell(
                'su 0 am broadcast -a android.intent.action.AIRPLANE_MODE --ez state true')
            time.sleep(6)
            print('The Start airplane is finished.')
        except:
            raise Exception('The start airplane is not finished.')

    # shutdown the airplane mode
    def stop_airplane(self):
        try:
            self._adb_shell('settings put global airplane_mode_on 0')
            self._adb_shell(
                'su 0 am broadcast -a android.intent.action.AIRPLANE_MODE --ez state false')
            time.sleep(15)
            print('The Stop airplane is finished.')
        except:
            raise Exception('The stop airplane is not finished.')

    # screenshot on mobile
    def screen(self, cmd):
        screenExecute = subprocess.Popen(
            str(cmd), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        stdout, stderr = screenExecute.communicate()
        # print(stdout)
        # print(stderr)

    # Save the screenshot to PC
    def save_to_local(self, cmd):
        screenExecute = subprocess.Popen(
            str(cmd), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        stdout, stderr = screenExecute.communicate()
        print(stdout)
        # print(stderr)

    def screen_time(self, screenshot):
        now = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
        path = screenshot + '_' + now + '.jpg'
        return path

    def backup_log(self):
        now = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
        os.system('mkdir ' + now)
        os.system('cp *.log ' + now + '/')
        os.system('cp *.jpg ' + now + '/')


if __name__ == '__main__':
    print('------------------------------------------------------------------------------')
    print('Created on 2020/08/10')
    print('Author: ZL Chen')
    print('Title: The Wireless LAN should be worked after the airplane mode by android 10.0 is switch on/off.')
    print('------------------------------------------------------------------------------')
    airplane = airplane_wlan_single()
    airplane.kill_extension_file('log')
    airplane.kill_extension_file('jpg')
    #cycle_time = int(input('Please input the \'Cycle Times\' you want : '))
    #gateway = input('Please input the gateway : ')
    cycle_time = int(sys.argv[1])
    gateway = sys.argv[2]
    for cycle in range(cycle_time):
        airplane.adb_command_set('svc power stayon true')
        os.system('echo ' + 'Cycle Times: ' + str(cycle + 1) + ' >> ping_server.log')
        print('Cycle Times: ' + str(cycle + 1))
        airplane.start_airplane()
        screen_time = airplane.screen_time('airplane_on_' + str(cycle + 1))
        airplane.screen(r'adb shell /system/bin/screencap -p /mnt/sdcard/' + screen_time)
        airplane.save_to_local(r'adb pull /mnt/sdcard/' + screen_time + ' ./' + screen_time)
        airplane.stop_airplane()
        screen_time = airplane.screen_time('airplane_off_' + str(cycle + 1))
        airplane.screen( r'adb shell /system/bin/screencap -p /mnt/sdcard/' + screen_time)
        airplane.save_to_local(r'adb pull /mnt/sdcard/' + screen_time + ' ./' + screen_time)
        airplane.adb_command_set('ping -w 4 ' + gateway)
        airplane.adb_response_get('0% packet loss')
        os.system('echo ' + 'Cycle Times: ' + str(cycle + 1) + ', Passed: ' + str(sum_pass) + ', Failed: ' + str(sum_fail) + ' >> ping_server.log')
        print('Cycle Times: ' + str(cycle + 1) + ', Passed: ' + str(sum_pass) + ', Failed: ' + str(sum_fail))
    os.system('echo ' + 'Total Cycle Times: ' + str(cycle_time) + ', Passed: ' + str(sum_pass) + ', Failed: ' + str(sum_fail) + ' >> ping_server.log')
    print('Total Cycle Times: ' + str(cycle_time) + ', Passed: ' + str(sum_pass) + ', Failed: ' + str(sum_fail))
    airplane.adb_command_set('rm -rf /mnt/sdcard/airplane_*.jpg')
    airplane.backup_log()
    airplane.kill('adb')