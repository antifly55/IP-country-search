def ip2num(ip):
    ans = 0
    for byte in ip.split('.'):
        ans = ans * 256 + int(byte)
    return ans

def num2ip(num):
    ans = []
    for _ in range(4):
        ans.append(str(num%256))
        num //= 256
    return '.'.join(ans[::-1])

def lower_bound(ipInfo, target):
    lo, hi = 0, len(ipInfo)
    while lo < hi:
        mid = (lo+hi)//2
        if target <= ipInfo[mid][1]:
            hi = mid
        else:
            lo = mid + 1
    return ipInfo[lo]

def verification(block, target):
    if block[0] <= target < block[1]:
        return True
    return False

def query(ipInfo, ip):
    ip = ip2num(ip)
    block = lower_bound(ipInfo, ip)

    if verification(block, ip):
        print(f'country code: {block[2]}')
    else:
        print('IP is not registered')

def build(csv_path):
    ipInfo = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        f.readline()
        while True:
            line = f.readline()
            if not line:
                break

            date, country, sip, dip, prefix, allo_date = line.split(',')
            ipInfo.append((ip2num(sip), ip2num(dip), country))
    ipInfo.sort()

    return ipInfo

if __name__ == '__main__':
    ipInfo = build('ipv4.csv')
    query(ipInfo, '202.6.95.0')