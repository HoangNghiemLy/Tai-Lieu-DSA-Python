def main():
    bang_bam = dict()
    import random
    for _ in range(18):
        khoa = random.randint(0,10)
        gia_tri = random.randint(0,100)
        print(f'*Thêm khóa = {khoa}, giá trị = {gia_tri}')
        #bang_bam.them(khoa,gia_tri)
        bang_bam[khoa] = gia_tri
        print(bang_bam)
        print()
    #for
    khoa = int(input('Nhập vào 1 khóa: '))
    #gia_tri = bang_bam.lay(khoa)
    gia_tri = bang_bam[khoa]
    print(f'Khóa ={khoa}, có giá trị = {gia_tri}')
#def 
if __name__ == '__main__':
    main()