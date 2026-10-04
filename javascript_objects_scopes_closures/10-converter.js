#!/usr/bin/node

exports.converter = function (base) {
  return function convert (nb) {
    if (nb >= base) {
      return convert(Math.floor(nb / base)) + (nb % base).toString(36);
    }

    return nb.toString(36);
  };
};
