/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    // 返回参数的长度
    return args.length
};

/**
 * argumentsLength(1, 2, 3); // 3
 */