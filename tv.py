class Tv:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1
        else:
            print('A tv está desligada')

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1
        else:
            print('A tv está desligada')


if __name__ == '__main__':
    televisao = Tv()
    print(f'Televisão está ligada: {televisao.ligada}')
    televisao.power()
    print(f'Televisão está ligada: {televisao.ligada}')
    televisao.aumenta_canal()
    print(f'A televisão está ligada no canal: {televisao.canal}')
    televisao.diminui_canal()
    televisao.diminui_canal()
    print(f'A televisão está ligada no canal: {televisao.canal}')
    televisao.power()
    print(f'Televisão está ligada: {televisao.ligada}')
    televisao.aumenta_canal()
    televisao.power()
    print(f'Televisão está ligada: {televisao.ligada}')
    televisao.aumenta_canal()
    print(f'A televisão está ligada no canal: {televisao.canal}')
