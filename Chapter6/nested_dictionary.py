GPU = {
    'GPU1': {
        'Name':'GTX 970',
        'VRam': '4 GB',
        'Brand': 'Geforce',
        'Clock Speed': 1051,
        },

    'GPU2': {
        'Name':"RX 470",
        'VRam': '4 GB',
        'Brand': 'Radeon',
        'Clock Speed': 1206,
        },

    'GPU3': {
        'Name':"RX 5700XT",
        'VRam': '8 GB',
        'Brand': 'Radeon',
        'Clock Speed': 1740,
        },

    'GPU4': {
        'Name':"RTX 2070",
        'VRam': '8 GB',
        'Brand': 'Geforce',
        'Clock Speed': 1620,
        },        
}


for gpu, info in GPU.items():
    print(f"\nGPU: {info['Name']}")
    vram =info['VRam']
    brand = info['Brand']
    clock = info['Clock Speed']

    print(f"\tVram: {vram}")
    print(f"\tBrand: {brand}")
    print(f"\tClock Speed: {clock}")


