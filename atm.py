
# Source Code by : CHARLY JOEZER
# Title          : Simple ATM Program Using Python
# Date           : 26-03-2023 (Last Update)
# Note           : I will update soon...
# Languange      : Bahasa (Indonesia)

import time
import os, sys

class Atm :
    def pilih_menu():
        data = {
            'saldo': 1000000,
            'pin'  : 123456,
        }
        nomor_va = {
            '1' : {
                    'nama' : 'BPJS',
                    'va' : '111'
                    },
            '2' : {
                    'nama' : 'Listrik',
                    'va' : '222'
                    },
            '3' : {
                    'nama' : 'PDAM',
                    'va' : '333'
                    },
        }
        
        check = True;
        while(check):
            os.system('cls')
            print("="*38)
            print("|           ATM BANK CHARLY          |")
            print("|        Jl.Konoha No.12 Rt.14       |")
            print("|            Telp: 14022             |")
            print("="*38)
            
            # MEMASUKAN PIN ATM
            totalEntry = 0;
            while(True) :
                if(totalEntry >= 3) :
                    print("Anda Melakukan kesalahan 3 kali!")
                    print("Sementara Rekening anda Diblokir")
                    print("Hubungi : 14022 (BANK CHARLY)")
                    print("="*38)
                    print('')                
                    exit()
                elif(totalEntry >= 1 and totalEntry < 3):
                    print('Total Kesalahan :',totalEntry)
                    print('Lebih dari 3 kali akan terblokir')
                    print("="*38)
                    print('')        

                PIN = str(input('Masukkan PIN Anda : '))
                print('Mohon Tunggu....')
                print('')
                time.sleep(1)
                os.system('cls')
                if(PIN == str(data['pin'])) :
                    break
                else :
                    totalEntry += 1
                    print("="*38)
                    print("PIN salah!")
            
            
            print("===========  MENU PILIHAN ===========")
            print('| [1] Informasi Saldo               |')
            print('| [2] Bayar                         |')
            print('| [3] Transfer                      |')
            print('| [4] Ambil Uang                    |')
            print('| [5] Keluar                        |')
            print("="*38)
            pilih = str(input('Masukan Pilihan Anda : '))
            print('')
            os.system('cls')
            
            
            # [1] INFORMASI SALDO
            if(pilih == '1'):
                print("="*38)
                print("Menu : Informasi Saldo")
                print("Saldo anda : Rp.",data['saldo'])
                print("="*38)
                
                transaksi_lagi = True
                while(transaksi_lagi):
                    lagi = input('Ingin Melakukan Transaksi lagi ? [y/t]: ')
                    if(lagi == 'y'):
                        check = True
                        transaksi_lagi = False
                    elif(lagi == 't'):
                        os.system('cls')
                        print("="*38)
                        print('Silahkan Ambil Kartu Anda....')
                        print('Terima Kasih')
                        print("="*38)
                        check = False
                        transaksi_lagi = False
                    else:
                        os.system('cls')
                        print('Pilihan tidak sesuai!')
                        transaksi_lagi = True  
                        
                        
            # [2] BAYAR
            elif(pilih == '2'):
                while(True) :
                    print("="*38)
                    print("Menu : Bayar")
                    print("[1].BPJS       [3].PDAM")
                    print("[2].Listrik    [4].Kembali")
                    print("="*38)
                    bayar = str(input('Masukan Pilihan Anda : '))
                    if(bayar == '1' or bayar == '2' or bayar == '3' ):
                        print('')
                        os.system('cls')
                        print("="*38)
                        print('Pembayaran :',nomor_va[bayar]['nama'])
                        print("="*38)
                        getNomorVa = str(input('Masukkan Nomor VA : '))
                        print('Mengecek Nomor Virtual Account...')
                        time.sleep(3)               
                        if(getNomorVa == nomor_va[bayar]['va']) :
                            jumlah = int(input('Masukkan Jumlah Pembayaran : '))
                            print("Memproses Pembayaran...")
                            time.sleep(4)
                            os.system('cls')
                            if(jumlah <= data['saldo'] and jumlah >= 0) :
                                data['saldo'] -= jumlah
                                print('')
                                print("="*38)
                                print('Pembayaran         :',nomor_va[bayar]['nama'])
                                print('Jumlah Pembayaran  : Rp.',jumlah)
                                print('Status             : Berhasil')
                                print('Sisa Saldo         : Rp.',data['saldo'])
                                print("="*38)
                                print('Pembayaran Anda Berhasil!')
                                print('')
                                break
                            elif(jumlah <= 0) :
                                os.system('cls')
                                print("="*38)
                                print('Pembayaran Minimal Rp.1 !!!')
                                print("="*38)
                                time.sleep(3)
                                os.system('cls')
                                continue
                            else : 
                                print('')
                                print("="*38)
                                print('Maaf, Saldo anda tidak cukup!')
                                print("="*38)
                                break
                        else :
                            os.system('cls')
                            print("="*38)
                            print('Nomor VA tidak sesuai !!!')
                            print("="*38)
                            time.sleep(2)
                            os.system('cls')
                            continue
                    elif(bayar == '4') :
                        break
                    else :
                        os.system('cls')
                        continue
                        
                    
                if(bayar == '4') :
                    check = True
                    continue
                
                transaksi_lagi = True
                while(transaksi_lagi):
                    lagi = input('Ingin Melakukan Transaksi lagi ? [y/t]: ')
                    if(lagi == 'y'):
                        check = True
                        transaksi_lagi = False
                    elif(lagi == 't'):
                        os.system('cls')
                        print("="*38)
                        print('Silahkan Ambil Kartu Anda....')
                        print('Terima Kasih')
                        print("="*38)
                        check = False
                        transaksi_lagi = False
                    else:
                        os.system('cls')
                        print('Pilihan tidak sesuai!')
                        transaksi_lagi = True
                
                
                
            # [3] TRANSFER
            elif(pilih == '3'):
                while(True) :
                    print("="*38)
                    print("Menu : Transfer")
                    print("[1].Transfer Sesama Bank")
                    print("[2].Transfer Antar Bank")
                    print("[3].Kembali")
                    print("="*38)
                    
                    transfer = str(input('Masukan Pilihan Anda : '))
                    if(transfer == '1' or transfer == '2'):
                        if(transfer == '2') :
                            while(True) :
                                os.system('cls')
                                print("="*38)
                                print('[1].BCA    [3].BNI')
                                print('[2].BRI    [4].Kembali')
                                print("="*38)
                                kodebank = str(input('Pilih Bank : '))
                                if(kodebank == '1') :
                                    kodebank = 'BCA'
                                    break
                                elif(kodebank == '2'):
                                    kodebank = 'BRI'
                                    break
                                elif(kodebank == '3'):
                                    kodebank = 'BNI'
                                    break
                                elif(kodebank == '4'):
                                    os.system('cls')
                                    break
                                else :
                                    os.system('cls')
                                    continue
                            if(kodebank == '4'):
                                os.system('cls')
                                continue
                                
                                    
                                
                        transfer_to = int(input('Masukkan Nomor Rekening : '))
                        jumlah = int(input('Masukkan Jumlah Transfer : '))
                        print('Sedang memproses....')
                        time.sleep(4)
                        os.system('cls')
                        if(jumlah <= data['saldo'] and jumlah >= 0):
                            data['saldo'] = data['saldo'] - jumlah
                            print('')
                            print("="*38)
                            print('No Rekening       :',transfer_to)
                            if(transfer == '2'):
                                print('Nama Bank         :',kodebank)
                            print('Nominal Transfer  : Rp.',jumlah)
                            print("Status            : BERHASIL")
                            print("="*38)
                            print('')
                            break
                        
                        elif(jumlah <= 0):
                            os.system('cls')
                            print("="*38)
                            print('Transfer Minimal Rp.1 !!!')
                            print("="*38)
                            time.sleep(3)
                            os.system('cls')
                            continue
                            
                        else:
                            print('')
                            print("="*38)
                            print("Saldo anda tidak cukup!")
                            print("="*38)
                            break
                               
                    elif(transfer == '3'):
                        break
                    else :
                        print('')
                        os.system('cls')
                        print("="*25)
                        print('Pilihan tidak sesuai !')
                        print("="*25)
                        time.sleep(2)
                        print('Kembali...')
                        time.sleep(2)
                        os.system('cls')
                        
                
                if(transfer == '3'):
                    print('test')
                    check = True
                    print('')
                    continue
            
                transaksi_lagi = True
                while(transaksi_lagi):
                    lagi = input('Ingin Melakukan Transaksi lagi ? [y/t]: ')
                    if(lagi == 'y'):
                        check = True
                        transaksi_lagi = False
                    elif(lagi == 't'):
                        os.system('cls')
                        print("="*38)
                        print('Silahkan Ambil Kartu Anda....')
                        print('Terima Kasih')
                        print("="*38)
                        check = False
                        transaksi_lagi = False
                    else:
                        print('Pilihan tidak sesuai!')
                        transaksi_lagi = True
                    
                    
                    
            # [4] AMBIL UANG
            elif(pilih == '4'):
                while(True) :
                    print("="*38)
                    print("Menu : Ambil Uang")
                    print('[1]. Ambil Uang')
                    print('[2]. Kembali')
                    print("="*38)
                    
                    pilihMenu = str(input('Masukkan Pilihan Anda : '))
                    if(pilihMenu == '1') :   
                        jumlah = int(input('Masukkan Jumlah Penarikan: '))
                        print('Sedang Memproses....')
                        time.sleep(2)
                        os.system('cls')
                        if(jumlah <= data['saldo'] and jumlah >= 50000):
                            data['saldo'] = data['saldo'] - jumlah
                            print('')
                            print("="*38)
                            print("Jumlah Penarikan : Rp.",jumlah)
                            print("Sisa saldo       : Rp.",data['saldo'])
                            print("Status           : BERHASIL")
                            print("="*37)
                            print('')
                            break
                        elif(jumlah <= 50000):
                            os.system('cls')
                            print("="*38)
                            print('Penarikan Minimal Rp.50000 !!!')
                            print("="*38)
                            time.sleep(3)
                            os.system('cls')
                            continue
                        else:
                            print("Saldo anda tidak cukup!")    
                    elif(pilihMenu == '2'):
                        check = True
                        break
                    else :
                        os.system('cls')
                        continue
                if(pilihMenu == '2'):
                    continue
                    
                    
                transaksi_lagi = True
                while(transaksi_lagi):
                    lagi = input('Ingin Melakukan Transaksi lagi ? [y/t]: ')
                    if(lagi == 'y'):
                        check = True
                        transaksi_lagi = False
                    elif(lagi == 't'):
                        os.system('cls')
                        print("="*38)
                        print('Silahkan Ambil Kartu Anda....')
                        print('Terima Kasih')
                        print("="*38)
                        check = False
                        transaksi_lagi = False
                    else:
                        print('Pilihan tidak sesuai!')
                        transaksi_lagi = True
                    
            # [5] KELUAR
            elif(pilih == '5'):
                check = False
                print('Silahkan Ambil Kartu Anda....')
                print('Terima Kasih :)')
                print("="*37)
                print('')
                exit()
        
Atm.pilih_menu()