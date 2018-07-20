$(function(){

  var model = {
    init: function() {
        data = [{name:"cat1", clickCount:0, src: "img/cat1.jpg"},
                {name:"cat2", clickCount:0, src: "img/cat2.jpg"},
                {name:"cat3", clickCount:0, src: "img/cat3.jpg"},
                {name:"cat4", clickCount:0, src: "img/cat4.jpg"},
                {name:"cat5", clickCount:0, src: "img/cat5.jpg"}]
    },

    getData:function(){
      return data;
    }
    
  };

  var octopus = {
    
    updateCurrentCat : function(){
      if(this.currentInd == model.getData().length) this.currentInd = 0;
      this.currentCat = model.getData()[this.currentInd]
    },
    
    getCatInd: function(){
      return model.data.indexOf(currentCat);
    },
    getCatCounter: function() {
      return this.currentCat.clickCount;
    },
    getCatName: function() {
      return this.currentCat.name;
    },
    getCatImg: function() {
      return this.currentCat.src;
    },
    incrementCounter: function() {
      this.currentCat.clickCount++;
      this.currentInd++;
      view.render();
    },
    saveNewCat: function(newCat) {
      model.getData().push(newCat);
    },

    init: function() {
      model.init();
      this.currentCat = model.getData()[0];
      this.currentInd = 0;
      view.init();
    }
  };

  var view = {
    init: function() {
        this.render();
        this.catImageElem = document.getElementById('imagecat');
        this.admBtn = document.getElementById('admBtn');
        this.cancelBtn = document.getElementById('cancelBtn');
        this.saveBtyn = document.getElementById('saveBtn');
        // on click, increment the current cat's counter
        this.catImageElem.addEventListener('click', function(){
          octopus.incrementCounter();
          octopus.updateCurrentCat();
        });

        this.admBtn.addEventListener('click', function(){
          $("#adminBlock").show();
        });

        this.cancelBtn.addEventListener('click', function(){
          $("#adminBlock").hide();
        });

        this.saveBtyn.addEventListener('click', function(){


          cat = { name:$("#name")[0].value,
                  clickCount: $("#newclicks")[0].value,
                  src: $("#url")[0].value}


          octopus.saveNewCat(cat)

        });
        
    },
    render: function(){

      $( "#clicks" )[0].innerHTML = octopus.getCatCounter();
      $( "#catname" )[0].innerHTML = octopus.getCatName();
      $("#imagecat").attr("src", octopus.getCatImg());

    }
  };
  octopus.init();

});