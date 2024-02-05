document.addEventListener('DOMContentLoaded', function () {
    const hamburger = document.querySelector('.hamburger');
    const navMenuContainer = document.querySelector('.nav-menu__container');
    const navLinks = document.querySelectorAll('.nav-link');

    hamburger.addEventListener('click', function () {
        hamburger.classList.toggle('active');
        navMenuContainer.classList.toggle('active');
    });

    navLinks.forEach(function (navLink) {
        navLink.addEventListener('click', function () {
            hamburger.classList.remove('active');
            navMenuContainer.classList.remove('active');
        });
    });
});

$(document).ready(function () {
    var currentPage = 1;
    var isAnimating = false;
    var popupOpened = localStorage.getItem("popupOpened"); // Проверяем, был ли попап уже открыт

    if (!popupOpened) {
        setTimeout(function () {
            $("#popup").fadeIn();
            showPage(currentPage);
            localStorage.setItem("popupOpened", "true"); // Устанавливаем флаг, что попап был открыт
        }, 5000);
    }

    $("#openpopup, .openpopup").click(function () {
        $("#popup").fadeIn();
        showPage(currentPage);
    });

    $("#popup").click(function (event) {
        if (!$(".popup-content").is(event.target) && $(".popup-content").has(event.target).length === 0) {
            $("#popup").fadeOut();
        }
    });


function send_form() {
    var checkedCheckboxes = document.querySelectorAll('.check_tags:checked');

    var radioText = '';
    var labelsText = [];

    for (var i = 0; i < checkedCheckboxes.length; i++) {
        var checkbox = checkedCheckboxes[i];
        var label = document.querySelector('label[for="' + checkbox.id + '"]');

        if (label) {
            var labelText = label.textContent;
            labelsText.push(labelText);
        }
    }


    var checkedRayon = document.querySelectorAll('.check_rayon:checked');

    var labelsRayon = [];

    for (var i = 0; i < checkedRayon.length; i++) {
        var checkbox = checkedRayon[i];
        var label = document.querySelector('label[for="' + checkbox.id + '"]');

        if (label) {
            var labelText = label.textContent;
            labelsRayon.push(labelText);
        }
    }



    var radioButtons = document.getElementsByName('format-radio');

    var selectedRadioButton;
    for (var i = 0; i < radioButtons.length; i++) {
        if (radioButtons[i].checked) {
            selectedRadioButton = radioButtons[i];
            break;
        }
    }

    var formatTitle = selectedRadioButton.parentElement.querySelector('.format-title').textContent;
    radioText += formatTitle;

    var data = {
        tag: labelsText.join(' '),
        city: $('#select_city').val(),
        rayon: labelsRayon.join(' '),
        resolution: radioText,
        email: $('#popup_email').val()
    }

    $.get('/ajax/voronka', {data}, function(data){
        console.log(data);
    });
}


    $(".nextButton").click(function () {
        if (!isAnimating) {
            isAnimating = true;
            currentPage++;
            if (currentPage < 6) {
                fadeOutCurrentPage(function () {
                    showPage(currentPage);
                });
            } else {
                if ($('#popup_email').val().length > 2) {
                  fadeOutCurrentPage(function () {
                    showPage(currentPage);
                    send_form();
                  });
                }
            }
        }
    });

    $(".closeButton").click(function () {
        fadeOutCurrentPage(function () {
            $("#popup").fadeOut();
        });
    });

    function showPage(pageNumber) {
        $(".popup-page").removeClass("active");
        var $currentPage = $(".popup-page[data-page=" + pageNumber + "]");
        $currentPage.addClass("active");
        $currentPage.fadeIn(function () {
            isAnimating = false;
        });
    }

    function fadeOutCurrentPage(callback) {
        var $currentPage = $(".popup-page.active");
        $currentPage.fadeOut(callback);
    }
});

$(document).ready(function () {
    $(".slider-container").each(function () {
      let currentIndex = 0;
      const slides = $(this).find(".slider-item");
      const totalSlides = slides.length;

      function showSlide(index) {
        slides.hide();
        slides.eq(index).fadeIn();
      }

      $(this).find(".next-slide").click(function () {
        currentIndex = (currentIndex + 1) % totalSlides;
        showSlide(currentIndex);
      });

      $(this).find(".prev-slide").click(function () {
        currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
        showSlide(currentIndex);
      });

      showSlide(currentIndex);
    });
  });

  $(document).ready(function() {
    // Функция для установки активной кнопки и блока контента
    function setActive(button, content) {
      button.addClass('active');
      content.addClass('active');
    }

    // Функция для сброса активных классов
    function resetActiveClasses() {
      const buttons = $('.btn-profile, .btn-favorite, .btn-subscribe');
      const contents = $('.lk-profile, .lk-favourites, .lk-subscribe');

      buttons.removeClass('active');
      contents.removeClass('active');
    }

    // Обработчик события для кнопки btn-profile
    $('.btn-profile').click(function() {
      resetActiveClasses();
      setActive($(this), $('.lk-profile'));
    });

    // Обработчик события для кнопки btn-favorite
    $('.btn-favorite').click(function() {
      resetActiveClasses();
      setActive($(this), $('.lk-favourites'));
    });

    // Обработчик события для кнопки btn-subscribe
    $('.btn-subscribe').click(function() {
      resetActiveClasses();
      setActive($(this), $('.lk-subscribe'));
    });
  });

  $(document).ready(function () {
    var $scrollToTopButton = $("#scrollToTopButton");
  
    // Прокручиваем страницу вверх при клике на кнопку
    $scrollToTopButton.click(function () {
      $("html, body").animate(
        {
          scrollTop: 0
        },
      );
    });
  });

  $(document).ready(function() {
    $(".btn-maps.active").click(function() {
        $(".btn-list").addClass("active");
        $(".btn-maps").removeClass("active");
        $(".locations-items").addClass("procent50");
        $(".locations-items-wrapper").addClass("procent50");
        $(".location-map").addClass("active");
        $(".locations-main").addClass("active");
        $(".location-title").addClass("none");
        $(".location").addClass("active");
        $("body").addClass("hidden");
        
        // Scroll to the top of the page
        $('html, body').animate({scrollTop: 0}, 'slow');
    });

    $(".btn-list").click(function() {
        $(".btn-maps").addClass("active");
        $(".btn-list").removeClass("active");
        $(".locations-items").removeClass("procent50");
        $(".locations-items-wrapper").removeClass("procent50");
        $(".location-map").removeClass("active");
        $(".locations-main").removeClass("active");
        $(".location-title").removeClass("none");
        $(".location").removeClass("active");
        $("body").removeClass("hidden");
        
        // Scroll to the top of the page
        $('html, body').animate({scrollTop: 0}, 'slow');
    });
});

class SlideStories {
  constructor(id) {
    this.slide = document.querySelector(`[data-slide="${id}"]`);
    if (!this.slide) {
        return;
    }
    this.active = 0;
    this.init();
  }

  activeSlide(index) {
    this.active = index;
    this.items.forEach((item) => {
      item.classList.remove("active");
    });
    this.items[index].classList.add("active");
    this.thumbItems.forEach((item) => {
      item.classList.remove("active");
    });
    this.thumbItems[index].classList.add("active");
  }

  prev() {
    if (this.active > 0) {
      this.activeSlide(this.active - 1);
    } else {
      this.activeSlide(this.items.length - 1);
    }
  }

  next() {
    if (this.active < this.items.length - 1) {
      this.activeSlide(this.active + 1);
    } else {
      this.activeSlide(0);
    }
  }

  addNavigation() {
    const nextBtn = this.slide.querySelector(".story-next");
    const prevBtn = this.slide.querySelector(".story-prev");
    nextBtn.addEventListener("click", this.next.bind(this));
    prevBtn.addEventListener("click", this.prev.bind(this));
  }

  addThumbItems() {
    this.items.forEach(() => (this.thumb.innerHTML += `<span></span>`));
    this.thumbItems = Array.from(this.thumb.children);
  }

  init() {
    this.items = this.slide.querySelectorAll(".story-items > *");
    this.thumb = this.slide.querySelector(".story-thumb");
    if (this.items.length === 0) {
        console.log(this.slide)
        return;
    } // Проверяем, что есть элементы для слайдов
    this.addThumbItems();
    this.activeSlide(0);
    this.addNavigation();
  }
}


$(document).ready(function() {
  const tagButton = $(".tag-color");
  const locationFilter = $(".location-filter");
  const blur = $(".blur");

  tagButton.click(function() {
      locationFilter.addClass("active");
      blur.addClass("active");
      $("body").css("overflow", "hidden"); // Добавляем стиль overflow: hidden
  });

  blur.click(function() {
      locationFilter.removeClass("active");
      blur.removeClass("active");
      $("body").css("overflow", "auto"); // Восстанавливаем прокрутку
  });

  locationFilter.on("touchstart", function(e) {
      const startY = e.originalEvent.touches[0].clientY;

      locationFilter.on("touchmove", function(e) {
          const currentY = e.originalEvent.touches[0].clientY;
          if (currentY - startY > 50) {
              locationFilter.removeClass("active");
              blur.removeClass("active");
              $("body").css("overflow", "auto"); // Включаем прокрутку
              locationFilter.off("touchmove");
          }
      });
  });
});

const block = document.querySelector('.block');
let isSwipedUp = false;

if (block) {
    block.addEventListener('touchstart', handleTouchStart);
    block.addEventListener('touchmove', handleTouchMove);
    block.addEventListener('touchend', handleTouchEnd);
}

        let touchStartY;

        function handleTouchStart(event) {
            touchStartY = event.touches[0].clientY;
        }

        function handleTouchMove(event) {
            const touchEndY = event.touches[0].clientY;
            const touchDistance = touchEndY - touchStartY;

            if (touchDistance < 0 && !isSwipedUp) {
                // Swipe up
                block.style.bottom = '0';
                isSwipedUp = true;
            } else if (touchDistance > 0 && isSwipedUp) {
                // Swipe down
                block.style.bottom = '-400px';
                isSwipedUp = false;
            }
        }

        function handleTouchEnd() {
            // Add any additional logic you may need here
        }


const scrollContainer = document.querySelector(".locations-similar");
const content = document.querySelector(".similar");

let isDragging = false;
let startX;

scrollContainer.addEventListener("mousedown", (e) => {
    isDragging = true;
    startX = e.clientX - content.scrollLeft;
    content.style.cursor = "grabbing";
});

scrollContainer.addEventListener("mouseup", () => {
    isDragging = false;
    content.style.cursor = "grab";
});

scrollContainer.addEventListener("mousemove", (e) => {
    if (!isDragging) return;
    const scrollX = e.clientX - startX;
    content.scrollLeft = scrollX;
});

scrollContainer.addEventListener("mouseleave", () => {
    isDragging = false;
    content.style.cursor = "grab";
});

document.getElementById("fileInput").addEventListener("change", function () {
  const fileName = this.files[0].name;
  document.getElementById("fileName").textContent = "Выбранный файл: " + fileName;
});


function wishlist(elem, num) {
    if ($(elem).data('wish') == 'add') {
        $.ajax({
            url: '/accounts/ajax/wishlist/',
            type: 'GET',
            data: {
                location: num
            },
            dataType: 'json',
            success: function(response) {
                $(elem).empty()
                $(elem).data('wish', 'delete')
                $(elem).append(`<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
                                                      <g opacity="0.9">
                                                          <path d="M12 20.3249C11.7667 20.3249 11.5292 20.2832 11.2875 20.1999C11.0458 20.1166 10.8333 19.9832 10.65 19.7999L8.925 18.2249C7.15833 16.6082 5.5625 15.0041 4.1375 13.4124C2.7125 11.8207 2 10.0666 2 8.1499C2 6.58324 2.525 5.2749 3.575 4.2249C4.625 3.1749 5.93333 2.6499 7.5 2.6499C8.38333 2.6499 9.21667 2.8374 10 3.2124C10.7833 3.5874 11.45 4.0999 12 4.7499C12.55 4.0999 13.2167 3.5874 14 3.2124C14.7833 2.8374 15.6167 2.6499 16.5 2.6499C18.0667 2.6499 19.375 3.1749 20.425 4.2249C21.475 5.2749 22 6.58324 22 8.1499C22 10.0666 21.2917 11.8249 19.875 13.4249C18.4583 15.0249 16.85 16.6332 15.05 18.2499L13.35 19.7999C13.1667 19.9832 12.9542 20.1166 12.7125 20.1999C12.4708 20.2832 12.2333 20.3249 12 20.3249Z" fill="#FF5D73"/>
                                                      </g>
                                                  </svg>`)
            },
            error: function(xhr, status, error) {
                console.log(error);
            }
        });
    } else {
        $.ajax({
            url: '/accounts/ajax/delete_wishlist/',
            type: 'GET',
            data: {
                location: num
            },
            dataType: 'json',
            success: function(response) {
                $(elem).empty()
                $(elem).data('wish', 'add')
                $(elem).append(`<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
                                                      <path d="M11.9998 20.7617L11.0056 19.8386C9.22104 18.1815 7.75214 16.7685 6.59892 15.5996C5.44571 14.4307 4.53449 13.3979 3.86527 12.5011C3.19604 11.6043 2.7345 10.7929 2.48065 10.0668C2.22682 9.3407 2.0999 8.61272 2.0999 7.88287C2.0999 6.42767 2.6016 5.2001 3.605 4.20015C4.6084 3.20018 5.83746 2.7002 7.29217 2.7002C8.17294 2.7002 9.01941 2.92231 9.83157 3.36655C10.6438 3.81078 11.3665 4.46367 11.9998 5.32522C12.6909 4.44317 13.4311 3.78515 14.2206 3.35117C15.01 2.91719 15.839 2.7002 16.7075 2.7002C18.1622 2.7002 19.3913 3.20018 20.3947 4.20015C21.3981 5.2001 21.8998 6.42767 21.8998 7.88287C21.8998 8.61272 21.7729 9.3407 21.519 10.0668C21.2652 10.7929 20.804 11.6036 20.1355 12.499C19.467 13.3945 18.5558 14.4273 17.4019 15.5975C16.2479 16.7678 14.7787 18.1815 12.9941 19.8386L11.9998 20.7617ZM11.9998 18.8078C13.6785 17.2698 15.0628 15.9533 16.1529 14.8583C17.2429 13.7634 18.104 12.8043 18.7362 11.9811C19.3684 11.1579 19.8104 10.4251 20.0623 9.7828C20.3143 9.14043 20.4402 8.50613 20.4402 7.8799C20.4402 6.81393 20.0893 5.92742 19.3874 5.22037C18.6854 4.51332 17.794 4.1598 16.7131 4.1598C15.8775 4.1598 15.0981 4.41845 14.3749 4.93575C13.6518 5.45306 13.0652 6.16749 12.6152 7.07902H11.3691C10.9229 6.17774 10.3342 5.46588 9.60282 4.94345C8.87147 4.42101 8.09938 4.1598 7.28655 4.1598C6.21208 4.1598 5.32229 4.51094 4.61717 5.21322C3.91204 5.91552 3.55947 6.8091 3.55947 7.89395C3.55947 8.51481 3.68595 9.14812 3.9389 9.79387C4.19185 10.4396 4.6364 11.172 5.27255 11.9909C5.9087 12.8099 6.76877 13.7681 7.85275 14.8655C8.93672 15.963 10.3191 17.2771 11.9998 18.8078Z" fill="white"/>
                                                  </svg>`)
            },
            error: function(xhr, status, error) {
                console.log(error);
            }
        });
    }

}


function wishlist_lk(elem, num) {
    $.ajax({
            url: '/accounts/ajax/delete_wishlist/',
            type: 'GET',
            data: {
                location: num
            },
            dataType: 'json',
            success: function(response) {
                $('#loc_'+num).remove()
            },
            error: function(xhr, status, error) {
                console.log(error);
            }
        });

}


// Получаем все чекбоксы с классом "check_tags"
var checkboxes = document.querySelectorAll('.check_tags');

// Добавляем обработчик события на изменение состояния каждого чекбокса
checkboxes.forEach(function(checkbox) {
    checkbox.addEventListener('change', function() {
        // Получаем метку (label) для данного чекбокса
        var label = document.querySelector('label[for="' + checkbox.id + '"]');

        // Если чекбокс активен, добавляем класс "active" к метке
        if (checkbox.checked) {
            label.classList.add('active');
        } else {
            // Если чекбокс не активен, удаляем класс "active" у метки
            label.classList.remove('active');
        }
    });
});


function change_city_location(elem) {
    if ($(elem).find('span').text() == 'Москва') {
        city = 'Екатеринбург'
    } else {
        city = 'Москва'
    }

    $.ajax({
      url: '/accounts/ajax/change_city/',
      type: 'GET',
      data: {
          city: city
      },
      dataType: 'json',
      success: function(response) {
          window.location.reload()
      },
      error: function(xhr, status, error) {
        console.log(error);
      }
    });
}

