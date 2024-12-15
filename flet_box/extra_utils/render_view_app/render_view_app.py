import subprocess
import os ,signal

class test_flet_app:
    """
    run_comand = test_flet_app(comands="whereis flet")
    run_comand.call_cmd(path='flet_box/extra_utils/settings_var/formulary_proyect.py')
    """

    full_cmd: list=[]
    desktop_view = ["-r"]
    web_view = ["-r","-w","-p","8080"]
    # middle_comand = "run"

    def __init__(self,
                 comands: str = "flet",
                 path_project: str = "",
                 ):
        super().__init__()
        self.search_cmd = f"whereis {comands}"

        self.comands = self.split_cmd(cmd=self.search_cmd,split=' ')

        # GET COMMAND WHEREIS FLET
        self.string_command = self.run_command()
        # print(self.string_command)
        self.full_cmd.clear()
        # GET ONLY PATH
        self.flet_path = self.split_cmd(cmd=self.string_command ,split=" ")[1]
        self.full_cmd.insert(0,self.flet_path)

        self.full_cmd.extend(self.desktop_view)
        self.full_cmd.append(path_project)
        # self.full_cmd.extend(self.web_view)

    def split_cmd(self,
                cmd: str="",
                split: str="",
                    ):

        return cmd.split(split)

    def run_command(self):
        self.terminal_output = subprocess.Popen(self.comands,stdout=subprocess.PIPE)
        self.data_captured = self.terminal_output.communicate()
        self.list_captured = str(self.data_captured[0],encoding="utf-8").split('\n')[0]

        return self.list_captured

    def call_cmd(self, call_cmd: str=""):

        if call_cmd:
            self.tmp_output = subprocess.run(call_cmd.split(' '))

        else:
            print(self.full_cmd)
            self.tmp_output = subprocess.run(self.full_cmd)

        return True

    def kill_cmd(self,pid):
        # kill_pid = self.terminal_output.pid
        # subprocess.Popen.kill(pid)
        data = pid.pid
        # os.kill(data, signal.SIGKILL)
        print(dir(pid))
        print(pid.send_signal(9))
        # pid.terminate()
        # for  i in range(7):
            # os.kill(data, signal.SIGKILL)
            #print(f'after: {pid.pid}')
            # data +=1
        # os.kill(pid.pid,signal.SIGKILL)
        # self.terminal_output.kill()
        # self.terminal_output.terminate()
        # print(kill_pid,'opther')

if __name__ == '__main__':

    run_comand = test_flet_app(comands="whereis flet")
    run_comand.call_cmd(path='flet_box/extra_utils/settings_var/formulary_proyect.py')


