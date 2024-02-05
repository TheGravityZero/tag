function program(num, code) {
    var d = ''
    var t = ''
    var lang = ''
    if (code == 'decode') {
        d += $('#enterCodeId').val()
        t += 'code'
    } else {
        d += $('#enterTextId').val()
        t += 'text'
    }
    if (num == 'smile') {
        lang += $('input[name="flexRadioDefault"]:checked').val()
    } else {
        lang += $('input[name="flexRadioDefault1"]:checked').val()
    }

    $.ajax({
        url: '/program_request',
        method: 'get',
        dataType: 'html',
        data: {
            text: d,
            type: t,
            func: num,
            lang: lang,
            number: $('#exampleFormControlInput1').val()
        },
        success: function(data){
            if (code == 'encode') {
                $('#enterCodeId').val(data);
                $('#reverseButton').attr("data-copy",data);
            } else {
                $('#enterTextId').val(data);
                $('#reverseButton').attr("data-copy",data);
            }
            $('#wh').attr("href", 'https://api.whatsapp.com/send?text='+data);
            $('#tg').attr("href", 'https://t.me/share/url?url='+data);
            $('#email').attr("href", 'mailto:?subject='+data);
        }
    });
}

function uniqSym(s) {
  var c = {};
  var r = '';

  for (var i = 0; i < s.length; i++) {
    if (!c[s[i]]) {
      r = r + s[i];
      c[s[i]] = 1;
    }
  }

  return r;
}

function indicator(text) {
    num = uniqSym(text)
    try {
        var lower = num.match(/[a-z]/g).length

    } catch (err) {
        try {
            var lower = num.match(/[а-яё]/g).length
        } catch (err) {
            var lower = 0
        }
    }
    try {
        var upper = num.match(/[A-Z]/g).length
    } catch (err) {
        try {
            var upper = num.match(/[А-ЯЁ]/g).length
        } catch (err) {
            var upper = 0
        }
    }



    if (20 < lower && lower < 33) {
        $('#button1').css('background-color', 'green')
        $('#button1_mob').css('background-color', 'green')
    } else {
        $('#button1').css('background-color', 'red')
        $('#button1_mob').css('background-color', 'red')
    }

    if (19 < upper && upper < 33) {
        $('#button2').css('background-color', 'green')
        $('#button2_mob').css('background-color', 'green')
    } else {
        if (9 < upper && upper < 20) {
            $('#button2').css('background-color', 'yellow')
            $('#button2_mob').css('background-color', 'yellow')
        } else {
            $('#button2').css('background-color', 'red')
            $('#button2_mob').css('background-color', 'red')
        }
    }
    $number_3 = 0
    if (num.indexOf(".") > -1) { $number_3 += 1; }
    if (num.indexOf(",") > -1) { $number_3 += 1; }
    if (num.indexOf("!") > -1) { $number_3 += 1; }
    if (num.indexOf("?") > -1) { $number_3 += 1; }
    if (num.indexOf("+") > -1) { $number_3 += 1; }
    if (num.indexOf("-") > -1) { $number_3 += 1; }
    if (num.indexOf(":") > -1) { $number_3 += 1; }
    if (num.indexOf(";") > -1) { $number_3 += 1; }
    if (num.indexOf("@") > -1) { $number_3 += 1; }
    if (num.indexOf(" ") > -1) { $number_3 += 1; }

    if (num.indexOf(1) > -1) { $number_3 += 1; }
    if (num.indexOf(2) > -1) { $number_3 += 1; }
    if (num.indexOf(3) > -1) { $number_3 += 1; }
    if (num.indexOf(4) > -1) { $number_3 += 1; }
    if (num.indexOf(5) > -1) { $number_3 += 1; }
    if (num.indexOf(6) > -1) { $number_3 += 1; }
    if (num.indexOf(7) > -1) { $number_3 += 1; }
    if (num.indexOf(8) > -1) { $number_3 += 1; }
    if (num.indexOf(9) > -1) { $number_3 += 1; }
    if (num.indexOf(0) > -1) { $number_3 += 1; }


    if ($number_3 > 10 && 31 > $number_3) {
        $('#button3').css('background-color', 'green')
        $('#button3_mob').css('background-color', 'green')
    } else {
        if ($number_3 > 0 && 11 > $number_3) {
            $('#button3').css('background-color', 'yellow')
            $('#button3_mob').css('background-color', 'yellow')
        } else {
            $('#button3').css('background-color', 'red')
            $('#button3_mob').css('background-color', 'red')
        }
    }

    $number_4 = 0
    if (num.indexOf("#") > -1) { $number_4 += 1; }
    if (num.indexOf("$") > -1) { $number_4 += 1; }
    if (num.indexOf("%") > -1) { $number_4 += 1; }
    if (num.indexOf("^") > -1) { $number_4 += 1; }
    if (num.indexOf('"') > -1) { $number_4 += 1; }
    if (num.indexOf("&") > -1) { $number_4 += 1; }
    if (num.indexOf("*") > -1) { $number_4 += 1; }
    if (num.indexOf("(") > -1) { $number_4 += 1; }
    if (num.indexOf(")") > -1) { $number_4 += 1; }
    if (num.indexOf("{") > -1) { $number_4 += 1; }
    if (num.indexOf("}") > -1) { $number_4 += 1; }
    if (num.indexOf("[") > -1) { $number_4 += 1; }
    if (num.indexOf("]") > -1) { $number_4 += 1; }
    if (num.indexOf("/") > -1) { $number_4 += 1; }
    if (num.indexOf("\\") > -1) { $number_4 += 1; }
    if (num.indexOf("'") > -1) { $number_4 += 1; }
    if (num.indexOf("|") > -1) { $number_4 += 1; }
    if (num.indexOf("~") > -1) { $number_4 += 1; }
    if (num.indexOf("`") > -1) { $number_4 += 1; }
    if (num.indexOf("<") > -1) { $number_4 += 1; }
    if (num.indexOf(">") > -1) { $number_4 += 1; }

    if ($number_4 > 10) {
        $('#button4').css('background-color', 'green')
        $('#button4_mob').css('background-color', 'green')
    } else {
        $('#button4').css('background-color', 'red')
        $('#button4_mob').css('background-color', 'red')
    }
}

const span = document.getElementById("reverseButton");

document.addEventListener('copy', function(e) {
  e.preventDefault();

  if (e.clipboardData) {
    e.clipboardData.setData('text/plain', $('#reverseButton').attr('data-copy'));
  } else if (window.clipboardData) {
    window.clipboardData.setData('Text', $('#reverseButton').attr('data-copy'));
  }
});

function triggerCopyEvent() {
  if (document.queryCommandSupported('copy')) {
    document.execCommand('copy');
  } else {
    alert('Команда копирования не поддерживается вашим браузером.');
  }
}

$('#reverseButton').on('click', triggerCopyEvent);



