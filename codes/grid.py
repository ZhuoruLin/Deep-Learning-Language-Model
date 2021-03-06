import os
import numpy
#Final Grid Search
emsizes = [300,500]
nhids = [300,500]
nlayers = 2
models = ['LSTM']
pdropouts = [0.5]
epochs = 40
for model in models:
    for emsize in emsizes:
        for nhid in nhids:
            for pdropout in pdropouts:
                save_path = '../../datasets/saved_models/%s_%s_%s_%s.pt' %(model,emsize,nhid,pdropout)
                info_path = '../../datasets/info_dict/%s_%s_%s_%s.pk' %(model,emsize,nhid,pdropout)
                cmdLine = 'python main.py --cuda --epochs %s --model %s --emsize %s --nhid %s\
                --save %s --infopath %s'%(epochs,model,emsize,nhid,save_path,info_path)
                print(cmdLine)
                os.system(cmdLine)




