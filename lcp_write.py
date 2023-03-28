import os 
import PySimpleGUI as sg
import subprocess

if __name__ == '__main__':
    # テーマの設定
    sg.theme('Black')

    # レイアウトの作成
    fp_layout = sg.Frame('Folder',[[sg.Text('ファイル>>', size=(15, 1), justification='left'),
                                    sg.InputText('', enable_events=True,),
                                    sg.FileBrowse('ファイル選択', key='input_file')]])
    bt_layout = sg.Frame('Button',[[sg.Submit(button_text='Start',font=('yu Gothic UI',8),size=(15,1),key='button1')]])
    in_layout = sg.Frame('Input',[[sg.Text('Port>>', size=(15, 1), justification='left'),sg.InputText("COM5",size=(31,0),key='input_port')],
                                  [sg.Text('Speed>>', size=(15, 1), justification='left'),sg.InputText("115200",size=(31,0),key='input_speed')],
                                  [sg.Text('Clock>>', size=(15, 1), justification='left'),sg.InputText("480000",size=(31,0),key='input_clock')],
                                  [sg.Text('Lpc>>', size=(15, 1), justification='left'),sg.InputText("lpc21isp_197\lpc21isp.exe",size=(31,0),key='lpc_path')]])
    read_box_layout = sg.Frame('Read',
                                [[sg.Multiline(size=(45,11),background_color='#111111',text_color='#ffffff',key='read_box',disabled=True,reroute_stdout=True,reroute_stderr=True)]],
                                element_justification='center')
    layout = [[fp_layout],
              [in_layout],
              [bt_layout],
              [read_box_layout]]
    
    # ウインドウの作成
    window = sg.Window('LCP Writer',layout)
    while True:
        event, values = window.read(timeout=1)
        # 終了
        if event is None:
            print('@exit')
            break
        # 書き込み
        if event == 'button1':
            file_path = values['input_file']
            if file_path != '':
                print("@Start")
                port = values['input_port']
                speed = values['input_speed']
                clock = values['input_clock']
                path = values['lpc_path']
                ret = subprocess.run([path, "-control", "-bin", file_path, port, speed, clock], shell=True)
                print("@End")
            else:
                print("@Error")

    window.close()