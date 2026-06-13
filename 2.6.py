# ханойські вежі факультету
import sys
sys.setrecursionlimit(10**6)


def move_disks(n, src='A', des='C', aux='B'):
    if n == 1:
        print(f"Move disk 1 from {src} to {des}")
        return
    move_disks(n - 1, src, aux, des)
    print(f"Move disk {n} from {src} to {des}")
    move_disks(n - 1, aux, des, src)


n = int(input())
move_disks(n)
