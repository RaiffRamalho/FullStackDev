var Cat = function(data) {

  this.clickCount = ko.observable(data.clickCount);
  this.name = ko.observable(data.name);
  this.imgSrc = ko.observable(data.imgSrc);
  this.imgAttribution = ko.observable(0);
  

  
  self.nickname = ko.observableArray([
    { name: 'Bert' },
    { name: 'Charles' },
    { name: 'Denise' }
  ]);
  
}

var ViewModel = function() {
  this.currentCat = ko.observable( new Cat({
    clickCount: 0,
    name: 'tabby',
    imgSrc: 'img/22252709_010df3379e_z.jpg'
  }));
  this.incrementCount = function() {
      this.clickCount( this.clickCount() + 1);
  };

  this.hasClickedTooManyTimes = ko.computed(function() {
    return this.currentCat().clickCount() >= 5 ? "too many click" : "you can click";
  }, this);

};

ko.applyBindings(new ViewModel());