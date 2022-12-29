M1 = f'\nMAL_ACCESS_TOKEN=AAAAA'
M2 = f'\nMAL_REFRESH_TOKEN=BBBBBB'

with open('.env', 'r+') as f:
    old = f.read()
    if not 'MAL' in str(old):
        f.writelines(M1 + M2)