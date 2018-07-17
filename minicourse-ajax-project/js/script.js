
function loadData() {

    var $body = $('body');
    var $wikiElem = $('#wikipedia-links');
    var $nytHeaderElem = $('#nytimes-header');
    var $nytElem = $('#nytimes-articles');
    var $greeting = $('#greeting');

    // clear out old data before new request
    $wikiElem.text("");
    $nytElem.text("");

    // load streetview

    var streetStr = $('#street').val();
    var cityStr = $('#city').val();
    var address = streetStr + ', ' + cityStr;

    $greeting.text('City: '+ address);

    var imgViewUrl = 'http://maps.googleapis.com/maps/api/streetview?size=600x300&location=' + address+'';

    $body.append('<img class="bgimg" src="'+imgViewUrl+'">');

    var url = "https://api.nytimes.com/svc/search/v2/articlesearch.json";
    url += '?' + $.param({
        'q': cityStr,
        'sort': 'newest', 
        'api-key': "8ce716c4af6c44f2ba264c0518917abd"
    });

    $.getJSON( url, function( data ) {
        var items = [];
        $.each( data, function( key, val ) {
          items.push( "<li id='" + key + "'>" + val + "</li>" );
        });
       
        $( "<ul/>", {
          "class": "my-new-list",
          html: items.join( "" )
        }).appendTo( "body" );
      });

    return false;
};

$('#form-container').submit(loadData);
