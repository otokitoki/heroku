var $box = $('.box');
var $button = $('.button');
var isAnimate = false;

$button.on('mousedown', function(){
  if (isAnimate) {
    return;
  }
  $('.rolling_image').attr('src', './images/竜巻.jpg');
  $button.val('アニメーション中');
  $box.addClass('animation');
  isAnimate = true;
});

$box.on('animationend', function(){
  $button.val('アニメーション開始')
  $box.removeClass('animation');
  $('.rolling_image').attr('src', './images/ryu.jpg');
  isAnimate = false;
});
