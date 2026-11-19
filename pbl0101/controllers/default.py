import datetime

def index():
    waktu_sekarang = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    teks_output = f"""
    HELLO WORLD<br>
    #PBW3B1PBL0101<br>
    251080200130 Muhamad Naufal Alfarizi<br>
    Framework Pilihan &rarr; Python [4] - Web2py<br>
    TIME : {waktu_sekarang}
    """
    return XML(teks_output)