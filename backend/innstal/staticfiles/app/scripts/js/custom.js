//Toggle menu

$(document).ready(function(){
  $(document).on('click', '[data-toggle="menu"]', function(){
    var trget =  $(this).data('target');
    $(this).toggleClass('active');
    $(document).find(trget).toggleClass('open');
  });

  //toggle input
  $(document).on('click', '[for="toggle_1"]', function(){
    if($('#toggle_1').is(':checked')){
      $('.toggle-off').removeClass('on');
      $('.toggle-on').addClass('on');
    }
    else{
      $('.toggle-on').removeClass('on');
      $('.toggle-off').addClass('on');
    }
  });

  $(document).on('click', '[data-toggle="sidemenu"]', function(){
    $(this).toggleClass('active');
    $(document).find('body').toggleClass('open');
  });


  //Password Show/hide
  $(document).on('click', '[data-toggle="password"]', function(){
    if($(this).hasClass("active")){
      var trget =  $(this).data('for');
      $(this).removeClass('active');
      $(document).find('[data-label="'+ trget +'"]').attr('type', 'password');
    }
    else{
      var trget2 =  $(this).data('for');
      $(this).addClass('active');
      $(document).find('[data-label="'+ trget2 +'"]').attr('type', 'text');
    }
  });


  //Height of graph
  var hei = $('.chart-section').height();
  $('.slider-contentbx').height(hei);
});