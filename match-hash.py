import os, sys, subprocess as sp

args = sys.argv[1:]

if len(args) > 3:
	sys.exit('Sorry, too many args...')
else:
    hashinfo = {
        'hash': '',
        'algo': 'SHA256',
        'file': '',
    }

    for i in args:
        if len(i) <= 12 : hashinfo['algo'] = i.upper()
        else:
            if os.path.isfile(i): hashinfo['file'] = i
            else: hashinfo['hash'] = i.upper()

    if not hashinfo['hash']:
        print()
        print(f'''powershell Get-FileHash -Algorithm {hashinfo["algo"]} "{hashinfo['file']}" | Select-Object HASH | Select -ExpandProperty Hash''')
        sp.run(f'''powershell Get-FileHash -Algorithm {hashinfo["algo"]} "{hashinfo['file']}" | Select-Object HASH | Select -ExpandProperty Hash''')
        # sp.Popen(f'''powershell Get-FileHash -Algorithm {hashinfo["algo"]} "{hashinfo['file']}" | Select-Object HASH | Select -ExpandProperty Hash''')
    else:
        hash_out = sp.run(f'''powershell Get-FileHash -Algorithm {hashinfo["algo"]} "{hashinfo['file']}" | Select-Object HASH | Select -ExpandProperty Hash''', capture_output=True, text=True).stdout

        if hashinfo['hash'] == hash_out.upper(): print("Hashes Match")
        else: print("Hashes don't match")
