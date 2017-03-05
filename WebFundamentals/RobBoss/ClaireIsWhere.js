var Claire = {
  location: [0, 0],

  reset: function() {
    Claire.location = [0, 0];
  },

  move: function(x, y) {
    Claire.location = [Claire.location[0] + x, Claire.location[1] + y];
    return Claire;
  },

  showX: function() {
    return Claire.location[0];
  },

  showY: function() {
    return Claire.location[1];
  },

  show: function() {
    console.log(Claire.showX() + ", " + Claire.showY());
  },

  distanceFromHome: function() {
    // a2 + b2 = c2
    return Math.sqrt(Math.pow(Claire.showX(),2) + Math.pow(Claire.showY(), 2));
  },

  distanceFromPoint: function(coordinates) {
    var d_x = Claire.showX() - coordinates[0];
    var d_y = Claire.showY() - coordinates[1];
    return Math.sqrt(Math.pow(d_x,2) + Math.pow(d_y, 2));
  }
}
