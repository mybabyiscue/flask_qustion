function bindCaptchaBtnClick() {
    $('#captcha-btn').click(function () {
        var $this = $(this); // 保存当前点击的按钮
        var email = $("input[name ='email']").val();
        if (!email) {
            alert('请输入邮箱');
            return;
        }
        // 通过js发送网络请求，ajax,Async javascript and xml
        $.ajax({
            url: '/user/captcha',
            type: 'POST',
            data: {
                "email": email
            },
            success: function (res) {
                var code = res['code'];
                if (res.code === 200) {
                    // 取消点击事件
                    $this.off('click');
                    // 倒计时
                    var count = 60;
                    var timer = setInterval(function () {
                        count--; // 倒计时
                        if (count === 0) {
                            $this.text('获取验证码'); // 改变按钮文字
                            $this.bind('click', bindCaptchaBtnClick); // 绑定点击事件
                            clearInterval(timer); // 清除定时器
                        } else {
                            $this.text(count + '秒后重新获取'); // 改变按钮文字
                        }
                    }, 1000);// 每隔一秒执行一次
                    alert('验证码发送成功');

                } else {
                    alert(res['message']);
                }
            }
        });
    });
}

// 等网页加载完成后再执行
$(function () {
    bindCaptchaBtnClick();
});