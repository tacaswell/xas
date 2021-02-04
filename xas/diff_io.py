

def extract_diffraction(db, uid):
    hdr = db[uid]
    stream=hdr.table(stream_name='primary', fill=True)
    return stream['pe1_image'][1]





