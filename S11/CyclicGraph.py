import matplotlib.pyplot as plt
import math

def triangular_scheduler():
    args ={'min_lr':0, 'max_lr':1, 'step_size':500, 'iterations':2000}
    cycles = math.floor(1 + (args['iterations']/(2 * args['step_size'])))
    start = 0
    for _ in range(cycles):
        plt.plot([start, start + args['step_size'], start + (2*args['step_size'])], [args['min_lr'], args['max_lr'], args['min_lr']], color = 'black')
        start += 2 * args['step_size']

    [plt.axhline(y = i, label = '{0} = {1}'.format(list(args.keys())[list(args.values()).index(i)], i), color = 'red') for i in [args['min_lr'], args['max_lr']]]
    plt.legend(loc='upper right', bbox_to_anchor = (1.3,1))
    plt.axis('off')
    plt.show()