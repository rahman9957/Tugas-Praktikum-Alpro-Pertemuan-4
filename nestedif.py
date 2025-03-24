# input
print('TARGET PENGIRIMAN')
pengiriman = int(input('masukkan total barang pengiriman : '))

# proses 
if pengiriman  >= 78 :
    status = 'SUKSES'
    if pengiriman >= 85 :
        kriteria = 'TERCAPAI'
    else :
        status = 'MENYELESAIKAN'
else  :
        status  = 'GAME OVER'
        kriteria = 'RUGI'

# output 
print('status :',status)
print ('kriteria :',kriteria)
print ('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    