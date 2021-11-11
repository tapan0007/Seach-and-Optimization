eps = 1e-10
def derivative(x):
    return np.array([2 * x[0] - x[1], -x[0] + 6 * x[1]])
    
def function(x):
    return x[0]*x[0] - x[0] * x[1] + 3 * x[1] * x[1] + 5

def gradient_descent(start_point, step_size):
    points_set = [start_point]
    x0 = np.array([start_point[i] for i in range(0, len(start_point))])
    func_value = [function(start_point)]
    iterations = [0]
    max_iter = 10000
    _iter = 0
    while _iter < max_iter:
        points_set.append((x0[0], x0[1]))
        func_value.append(function(x0))
        iterations.append(_iter)
        print("Iteration: " + str(_iter) + ": Value at " + str(x0) + " " + "is " +  str(function(x0)) )
        gradient = derivative(x0)
        if gradient.max() < eps:
            break
        x1 = x0 - step_size*gradient
        x0 = x1
        _iter += 1

    print("Optimal value of function is " +  str(function(x1)) + " at x = " + str(x0) )
    return (points_set, func_value, iterations)
                         
points_set, func_value, iterations = gradient_descent((2,2), 0.3)
