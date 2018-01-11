//Toggle menu

$(document).ready(function(){
  $(document).on('click', '[data-toggle="menu"]', function(){
    var trget =  $(this).data('target');
    $(this).toggleClass('active');
    $(document).find(trget).toggleClass('open');
  });


  $(document).on('click', '[for="toggle_1"]', function(){
    if($('#toggle_1').is(':checked')){
      $('.toggle-off').removeClass('on');
      $('.toggle-on').addClass('on');
    }
    else{
      $('.toggle-on').removeClass('on');
      $('.toggle-off').addClass('on');
    }
  })
});