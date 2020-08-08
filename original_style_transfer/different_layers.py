import os
import time
from original_style_transfer.transfer_torch import main

possible_layers = [f'conv_{n}' for n in range(1, 6)]

results_folder = 'original_style_transfer/results'
if not os.path.isdir(results_folder):
    os.mkdir(results_folder)

# for l in possible_layers:
#     output = main(content_layers=[l], num_steps=50, style_weight=1e-6)
#     output.save(f'{results_folder}/content_{l}.jpg')

# for l in possible_layers:
#     output = main(style_layers=[l], num_steps=300, content_weight=1e-12)
#     output.save(f'{results_folder}/style_{l}.jpg')

start = time.time()
output = main()
output.save(f'{results_folder}/output.jpg')
print('Output time', time.time()-start)