////////////////////// Start Load /////////////////////
// منع التمرير أثناء تحميل الصفحة
document.body.style.overflow = "hidden";

window.addEventListener('load', () => {
    const loader = document.getElementById('loader');  // الحصول على العنصر الذي يحمل الـ id "loader"
    loader.classList.add('vanish-mode');  // إضافة الـ class لإخفاء اللودر بشكل تدريجي

    // السماح بالتمرير بعد اختفاء اللودر
    setTimeout(() => {
        document.body.style.overflow = "auto";
    }, 500);  // يطابق مدة الـ transition في CSS
});
////////////////////// End Load /////////////////////


////////////////////// start carousel /////////////////////
// const slides_ads = document.querySelectorAll(".slide_ads");
// let currentIndex = 0;
// let autoplayEnabled = true;
// let timeout;
// let isDragging = false;
// let startX;

// تحقق من أول زيارة في الجلسة
// if (sessionStorage.getItem("carouselShown") === "yes") {
//     document.querySelector(".overlay_ads").style.display = "none";
// } else {
//     sessionStorage.setItem("carouselShown", "yes");
//     document.querySelector(".overlay_ads").style.display = "flex";
// }

// function updateslides_ads() {
//     slides_ads.forEach((slide_ads, index) => {
//         let offset = index - currentIndex;
//         if (offset > Math.floor(slides_ads.length / 2)) {
//             offset -= slides_ads.length;
//         } else if (offset < -Math.floor(slides_ads.length / 2)) {
//             offset += slides_ads.length;
//         }

//         const translateX = offset * 220;
//         const scale = offset === 0 ? 1 : 0.7;
//         const rotateY = offset * 20;
//         const opacity = offset === 0 ? 1 : 0;  // Hide other slides
//         const zIndex = offset === 0 ? 2 : 1;

//         slide_ads.style.transition = "transform 0.6s ease, opacity 0.6s ease";
//         slide_ads.style.transform = `translateX(${translateX}px) scale(${scale}) rotateY(${rotateY}deg)`;
//         slide_ads.style.opacity = opacity;
//         slide_ads.style.zIndex = zIndex;
//     });
// }

// function nextslide_ads() {
//     if (currentIndex < slides_ads.length - 1) {
//         currentIndex++;
//     } else {
//         currentIndex = 0;
//     }
//     updateslides_ads();
// }

// function prevslide_ads() {
//     if (currentIndex > 0) {
//         currentIndex--;
//     } else {
//         currentIndex = slides_ads.length - 1;
//     }
//     updateslides_ads();
// }

// document.querySelector(".text-next").addEventListener("click", () => {
//     stopAutoplay();
//     nextslide_ads();
// });

// document.querySelector(".text-prev").addEventListener("click", () => {
//     stopAutoplay();
//     prevslide_ads();
// });

// function startAutoplay() {
//     if (autoplayEnabled) {
//         timeout = setTimeout(() => {
//             nextslide_ads();
//             startAutoplay();
//         }, 10000);
//     }
// }

// function stopAutoplay() {
//     clearTimeout(timeout);
//     autoplayEnabled = false;
//     setTimeout(() => {
//         autoplayEnabled = true;
//         startAutoplay();
//     }, 120000);
// }

// إغلاق الكاروسيل
// document.querySelector(".close-button-ads").addEventListener("click", () => {
//     document.querySelector(".overlay_ads").style.display = "none";
// });

// سحب/لمس
// document.querySelector(".carousel-container").addEventListener("mousedown", (e) => {
//     isDragging = true;
//     startX = e.clientX;
// });

// document.addEventListener("mouseup", () => {
//     isDragging = false;
// });

// document.addEventListener("mousemove", (e) => {
//     if (!isDragging) return;
//     if (e.clientX - startX > 50) {
//         prevslide_ads();
//         stopAutoplay();
//         isDragging = false;
//     } else if (e.clientX - startX < -50) {
//         nextslide_ads();
//         stopAutoplay();
//         isDragging = false;
//     }
// });

// document.addEventListener("touchstart", (e) => {
//     isDragging = true;
//     startX = e.touches[0].clientX;
// });

// document.addEventListener("touchend", () => {
//     isDragging = false;
// });

// document.addEventListener("touchmove", (e) => {
//     if (!isDragging) return;
//     if (e.touches[0].clientX - startX > 50) {
//         prevslide_ads();
//         stopAutoplay();
//         isDragging = false;
//     } else if (e.touches[0].clientX - startX < -50) {
//         nextslide_ads();
//         stopAutoplay();
//         isDragging = false;
//     }
// });

// updateslides_ads();
// startAutoplay();
////////////////////// End carousel /////////////////////


////////////////////// Start Install App /////////////////////
let deferredPrompt;

// التعامل مع تثبيت التطبيق على أندرويد
window.addEventListener('beforeinstallprompt', (event) => {
    event.preventDefault();
    deferredPrompt = event;
    document.getElementById('install-btn').style.display = 'block';

    document.getElementById('install-btn').addEventListener('click', () => {
        deferredPrompt.prompt();
        deferredPrompt.userChoice.then((choiceResult) => {
            if (choiceResult.outcome === 'accepted') {
                console.log('تم تثبيت التطبيق');
                document.getElementById('install-btn').style.display = 'none'; // إخفاء الزر بعد التثبيت
                localStorage.setItem('appInstalled', 'true'); // تخزين حالة التثبيت
            } else {
                console.log('تم إلغاء التثبيت');
            }
            deferredPrompt = null;
        });
    });
});

// إخفاء زر التثبيت عند اكتمال التثبيت على أندرويد
window.addEventListener('appinstalled', () => {
    console.log('التطبيق مثبت بالفعل');
    document.getElementById('install-btn').style.display = 'none'; // إخفاء زر أندرويد
    document.getElementById('ios-install-btn').style.display = 'none'; // إخفاء زر iPhone
    localStorage.setItem('appInstalled', 'true'); // تخزين حالة التثبيت
});

// التحقق إذا كان الجهاز iPhone لإظهار زر التثبيت الخاص به
function isIOS() {
    return /iPhone|iPad|iPod/i.test(navigator.userAgent);
}

// التحقق عند تحميل الصفحة إذا كان التطبيق مثبتًا مسبقًا
if (localStorage.getItem('appInstalled')) {
    document.getElementById('install-btn').style.display = 'none'; // إخفاء زر أندرويد
    document.getElementById('ios-install-btn').style.display = 'none'; // إخفاء زر iPhone
} else if (isIOS()) {
    let iosInstallBtn = document.getElementById('ios-install-btn');
    iosInstallBtn.style.display = 'block';

    iosInstallBtn.addEventListener('click', function () {
        alert("لتثبيت التطبيق على iPhone:\n" +
            "1. افتح الموقع في Safari.\n" +
            "2. اضغط على زر المشاركة.\n" +
            "3. اختر 'إضافة إلى الشاشة الرئيسية'.");

        // حفظ حالة التثبيت وإخفاء الزر
        localStorage.setItem('appInstalled', 'true');
        iosInstallBtn.style.display = 'none';
    });
}

// تسجيل Service Worker
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('service-worker.js')
        .then(() => console.log("Service Worker Registered"))
        .catch(err => console.log("Service Worker Failed", err));
}
////////////////////// End Install App /////////////////////



////////////////////// start Slider /////////////////////
var counter = 1;
setInterval(function () {
    document.getElementById('radio' + counter).checked = true;
    counter++;
    if (counter > 3) {
        counter = 1;
    }
}, 5000);
////////////////////// start Slider /////////////////////
function toggleMenu(element) {
    // إغلاق جميع القوائم
    document.querySelectorAll('.menu-icon-branchicon').forEach(function (icon) {
        if (icon !== element) {
            icon.classList.remove('active');
        }
    });

    // فتح أو إغلاق العنصر الحالي
    element.classList.toggle('active');
}

// إغلاق القائمة عند الضغط خارجها
document.addEventListener('click', function (e) {
    document.querySelectorAll('.menu-icon-branch').forEach(function (icon) {
        if (!icon.contains(e.target)) {
            icon.classList.remove('active');
        }
    });
});
////////////////////// start Language /////////////////////
var languagespan = document.getElementById('languagespan');
var languageMenu = document.getElementById('languageMenu');
var closeButton = document.getElementById('closeButton');
var languageItems = document.querySelectorAll('#languageMenu ul li');
var overlay_language = document.getElementById('overlay_language'); // الخلفية المعتمة

// إظهار القائمة مع الخلفية المعتمة
languagespan.addEventListener('click', function () {
    languageMenu.classList.add('visible');
    overlay_language.classList.add('active');
    document.body.style.overflow = 'hidden'; // منع التمرير
});

// إخفاء القائمة عند الضغط على زر الإغلاق
closeButton.addEventListener('click', closeMenu);

// إخفاء القائمة عند الضغط على الخلفية المعتمة
overlay_language.addEventListener('click', closeMenu);

// إخفاء القائمة عند الضغط خارجها
document.addEventListener('click', function (event) {
    if (!languageMenu.contains(event.target) && event.target !== languagespan) {
        closeMenu();
    }
});

// تغيير النص مع الاحتفاظ بالأيقونة عند اختيار اللغة
languageItems.forEach(function (item) {
    item.addEventListener('click', function () {
        var selectedLanguage = item.textContent; // الحصول على النص الجديد للغة
        languagespan.innerHTML = selectedLanguage + ' <i class="fa-solid fa-globe"></i>'; // تغيير النص مع الاحتفاظ بالأيقونة
        closeMenu();
    });
});

// دالة لإغلاق القائمة وإزالة التأثيرات
function closeMenu() {
    languageMenu.classList.remove('visible');
    overlay_language.classList.remove('active');
    document.body.style.overflow = ''; // إعادة التمرير
}

////////////////////// End Language /////////////////////

////////////////////// start Open Img Profile /////////////////////
// فتح الصورة في نافذة العرض
function openImage(element) {
    const overlay = document.getElementById("overlay");
    const overlayImg = document.getElementById("overlay-img");
    overlayImg.src = element.src; // نسخ رابط الصورة المختارة
    overlay.style.display = "flex"; // عرض النافذة
    document.body.style.overflow = "hidden"; // تعطيل التمرير
}

// إغلاق نافذة العرض
function closeImage(event) {
    if (event?.target?.id === "overlay" || !event) {
        const overlay = document.getElementById("overlay");
        overlay.style.display = "none"; // إخفاء النافذة
        document.body.style.overflow = "auto"; // إعادة التمرير
    }
}
////////////////////// End Open Img Profile /////////////////////

////////////////////// start Open Work Time and Footer /////////////////////
document.querySelectorAll(".openPopup").forEach(button => {
    button.addEventListener("click", () => {
        const popupId = button.getAttribute("data-popup");
        const popupOverlay = document.getElementById(popupId);

        popupOverlay.style.display = "flex";
        setTimeout(() => {
            popupOverlay.style.opacity = "1";
            popupOverlay.querySelector(".popup").style.transform = "scale(1)";
        }, 10);

        // تعطيل التمرير عند فتح النافذة
        document.documentElement.style.overflow = "hidden";
    });
});

function closeModal(popupId) {
    const popupOverlay = document.getElementById(popupId);

    popupOverlay.style.opacity = "0";
    popupOverlay.querySelector(".popup").style.transform = "scale(0.8)";

    setTimeout(() => {
        popupOverlay.style.display = "none";

        // إعادة التمرير عند إغلاق النافذة
        document.documentElement.style.overflow = "";
    }, 300);
}

document.querySelectorAll(".close-btn").forEach(button => {
    button.addEventListener("click", () => {
        const popupId = button.getAttribute("data-close");
        closeModal(popupId);
    });
});

document.querySelectorAll(".popup-overlay").forEach(overlay => {
    overlay.addEventListener("click", (event) => {
        if (event.target === overlay) {
            closeModal(overlay.id);
        }
    });
});
////////////////////// End Open Work Time and Footer /////////////////////

////////////////////// Start /////////////////////
function toggleContent() {
    let block1 = document.getElementById("block1");
    let block2 = document.getElementById("block2");
    let toggleButton = document.querySelector(".random2");

    block1.classList.toggle("active");
    block2.classList.toggle("active");
    toggleButton.classList.toggle("active");
}
////////////////////// End /////////////////////

////////////////////// Start According /////////////////////
document.addEventListener("DOMContentLoaded", function () {
    checkURLParams();
});

function openAccordion(id) {
    const targetAccordion = document.getElementById(id);

    if (!targetAccordion) {
        console.warn("العنصر غير موجود:", id);
        return;
    }

    // فتح الـ Accordion
    toggleAccordion(id);

    // الانتظار قليلاً حتى يُفتح العنصر قبل التمرير
    setTimeout(() => {
        let offset = 200; // تعويض بسبب القائمة العلوية
        let elementPosition = targetAccordion.getBoundingClientRect().top + window.scrollY;
        let offsetPosition = elementPosition - offset;

        window.scrollTo({
            top: offsetPosition,
            behavior: "smooth"
        });
    }, 300); // تأخير بسيط للتأكد من أن الـ Accordion مفتوح
}

function toggleAccordion(id, element) {
    const accordions = document.querySelectorAll('.accordion-content');
    const icons = document.querySelectorAll('.accordion-icon');

    // إغلاق جميع الأكورديونات المفتوحة
    accordions.forEach(function (accordion) {
        if (accordion.id !== id) {
            accordion.style.maxHeight = "0px";
            accordion.style.opacity = "0";
            setTimeout(() => {
                accordion.classList.remove("active");
            }, 300);
        }
    });

    // إعادة ضبط الأيقونات
    icons.forEach(function (icon) {
        icon.classList.remove("icon-rotated");
    });

    const currentAccordion = document.getElementById(id);
    if (!currentAccordion) return;

    const icon = element ? element.querySelector(".accordion-icon") : null;

    if (currentAccordion.classList.contains("active")) {
        // إغلاق العنصر الحالي
        currentAccordion.style.maxHeight = "0px";
        currentAccordion.style.opacity = "0";
        setTimeout(() => {
            currentAccordion.classList.remove("active");
        }, 300);
        if (icon) icon.classList.remove("icon-rotated");
    } else {
        // فتح العنصر الحالي
        currentAccordion.classList.add("active");
        currentAccordion.style.maxHeight = currentAccordion.scrollHeight + "px"; // ⬅️ تحديد الطول تلقائيًا
        currentAccordion.style.opacity = "1";
        if (icon) icon.classList.add("icon-rotated");
    }
}
////////////////////// End According /////////////////////

//////////////////////  Start Description  /////////////////////
function togglePopup(id) {
    const popup = document.getElementById(id);
    if (!popup) return;

    popup.classList.toggle("active");

    const anyPopupActive = document.querySelector(".popup-container.active");

    if (anyPopupActive) {
        document.body.classList.add("popup-open");
    } else {
        document.body.classList.remove("popup-open");
    }
}

function closePopup(event, id) {
    // التحقق من أن النقر تم على العنصر المحيط بالـ popup
    if (event.target.id === id) {
        togglePopup(id);
    }
}


function openSharePopup(productId, imageSrc, productName) {
    // تحديد الوضع الحالي (grid أو accordion)
    const isGrid = document.getElementById("block2")?.classList.contains("active");
    const viewMode = isGrid ? "grid" : "accordion";

    currentProductUrl = window.location.origin + window.location.pathname +
        "?product=" + encodeURIComponent(productId) +
        "&view=" + viewMode;

    // تحديث روابط المشاركة
    document.getElementById("whatsapp-share").href = "https://wa.me/?text=" + encodeURIComponent(currentProductUrl);
    document.getElementById("facebook-share").href = "https://www.facebook.com/sharer/sharer.php?u=" + encodeURIComponent(currentProductUrl);
    document.getElementById("messenger-share").href = "https://www.messenger.com/t/?link=" + encodeURIComponent(currentProductUrl);
    document.getElementById("telegram-share").href = "https://t.me/share/url?url=" + encodeURIComponent(currentProductUrl);
    document.getElementById("twitter-share").href = "https://twitter.com/intent/tweet?url=" + encodeURIComponent(currentProductUrl);
    document.getElementById("linkedin-share").href = "https://www.linkedin.com/sharing/share-offsite/?url=" + encodeURIComponent(currentProductUrl);
    document.getElementById("snapchat-share").href = "https://www.snapchat.com/scan?attachmentUrl=" + encodeURIComponent(currentProductUrl);
    document.getElementById("tiktok-share").href = "https://www.tiktok.com/share?url=" + encodeURIComponent(currentProductUrl);

    // تحديث صورة واسم المنتج
    document.getElementById("shareImage").src = imageSrc;
    document.getElementById("shareProductName").textContent = productName;

    // إظهار نافذة الشير
    document.getElementById("share-popup-container").classList.add("active");
    document.body.style.overflow = "hidden";
}



function closeSharePopup(event) {
    var container = document.getElementById("share-popup-container");
    if (!event || event.target === container) {
        container.classList.remove("active");
        document.body.style.overflow = "auto";
    }
}

function copyLink(button) {
    if (!currentProductUrl) {
        console.error("لم يتم العثور على رابط المنتج!");
        return;
    }

    if (navigator.clipboard) {
        navigator.clipboard.writeText(currentProductUrl).then(() => {
            showCopySuccess(button);
        }).catch(err => {
            console.error("فشل في النسخ", err);
            showCopyFailure(button);
        });
    } else {
        var tempInput = document.createElement("input");
        document.body.appendChild(tempInput);
        tempInput.value = currentProductUrl;
        tempInput.select();
        document.execCommand("copy");
        document.body.removeChild(tempInput);
        showCopySuccess(button);
    }
}

function showCopySuccess(button) {
    const icon = button.querySelector("i"); // الحصول على الأيقونة
    const text = button.querySelector("span"); // الحصول على النص

    icon.classList.remove("fa-copy"); // إزالة أيقونة النسخ
    icon.classList.add("fa-check"); // إضافة أيقونة الصح
    text.textContent = "تم النسخ"; // تغيير النص
    // text.textContent = "تم النسخ ✅"; // تغيير النص

    // button.classList.add("bg-green-500", "text-white");

    setTimeout(() => {
        icon.classList.remove("fa-check");
        icon.classList.add("fa-copy");
        text.textContent = "نسخ الرابط";
        // button.classList.remove("bg-green-500", "text-white");
    }, 2000);
}

function showCopyFailure(button) {
    const icon = button.querySelector("i");
    const text = button.querySelector("span");

    icon.classList.remove("fa-copy");
    icon.classList.add("fa-times");
    text.textContent = "فشل النسخ ❌";

    // button.classList.add("bg-red-500", "text-white");

    setTimeout(() => {
        icon.classList.remove("fa-times");
        icon.classList.add("fa-copy");
        text.textContent = "نسخ الرابط";
        // button.classList.remove("bg-red-500", "text-white");
    }, 2000);
}

function checkURLParams() {
   var urlParams = new URLSearchParams(window.location.search);
     var product = urlParams.get("product");
     var viewMode = urlParams.get("view");

     // تغيير طريقة العرض حسب البراميتر
     if (viewMode === "grid") {
         document.getElementById("block1")?.classList.remove("active"); // إخفاء accordion
         document.getElementById("block2")?.classList.add("active");    // إظهار grid
         document.querySelector(".random2")?.classList.add("active");
     } else if (viewMode === "accordion") {
         document.getElementById("block2")?.classList.remove("active"); // إخفاء grid
         document.getElementById("block1")?.classList.add("active");    // إظهار accordion
         document.querySelector(".random2")?.classList.remove("active");
     }

     if (product) {
         setTimeout(() => {
            let popupId = viewMode === "grid" ? "popup-grid-" + product : "popup-" + product;
const popupElement = document.getElementById(popupId);
const productElement = document.querySelector('[data-products*="' + product + '"]');

if (productElement) {
    productElement.scrollIntoView({ behavior: "smooth", block: "center" });
}

if (popupElement) {
    togglePopup(popupId);
} else {
    console.warn("العنصر غير موجود:", popupId);
}


             // لو كانت accordion فعل القسم
             if (viewMode === "accordion") {
                 const accordionElement = document.querySelector('[data-products*="' + product + '"]');
                 if (accordionElement) {
                     const sectionId = accordionElement.id;
                     const customBox = document.querySelector('[onclick*="' + sectionId + '"]');
                     if (customBox) {
                         toggleAccordion(sectionId, customBox);
                     } else {
                         toggleAccordion(sectionId);
                     }
                 }
             }

         }, 600);

         // إزالة البراميتر من الرابط بعد الفتح
         setTimeout(() => {
             var newUrl = window.location.origin + window.location.pathname;
             window.history.replaceState({}, document.title, newUrl);
         }, 1500);
     }
 }

















//////////////////////  End Description  /////////////////////

//////////////////////  Start Description Size  /////////////////////
document.querySelectorAll('.size-options button').forEach(button => {
    button.addEventListener('click', function () {
        let targetId = this.getAttribute('data-target');
        let priceDisplay = document.getElementById(targetId);
        priceDisplay.textContent = this.getAttribute('data-price');
    });
});
//////////////////////  End Description Size  /////////////////////


let linkBranch = '';

function openPopX(link) {
    linkBranch = link;
    document.getElementById("popup_share_branch").style.display = "flex";

    let encodedLink = encodeURIComponent(linkBranch);

    document.getElementById("Facebook-1").href = `https://www.facebook.com/sharer/sharer.php?u=${encodedLink}`;
    document.getElementById("twiter-1").href = `https://twitter.com/intent/tweet?url=${encodedLink}`;
    document.getElementById("WhatsApp-1").href = `https://wa.me/?text=${encodedLink}`;
    document.getElementById("Telegram-1").href = `https://t.me/share/url?url=${encodedLink}`;
    document.getElementById("Messenger-1").href = `https://www.facebook.com/dialog/send?link=${encodedLink}&app_id=123456789`;
    document.getElementById("TikTok-1").href = `https://www.tiktok.com/share?url=${encodedLink}`;
    document.getElementById("Snapchat-1").href = `https://www.snapchat.com/share?url=${encodedLink}`;
    document.getElementById("LinkedIn-1").href = `https://www.linkedin.com/sharing/share-offsite/?url=${encodedLink}`;
}

function closePopX() {
    document.getElementById("popup_share_branch").style.display = "none";
}

function copyLinkB12() {
    if (linkBranch) {
        navigator.clipboard.writeText(linkBranch).then(() => {
            let msg = document.getElementById("copiedMsg");
            msg.style.display = "block";
            setTimeout(() => {
                msg.style.display = "none";
            }, 2000);
        });
    }
}

document.getElementById("popup_share_branch").addEventListener("click", function (e) {
    if (e.target === this) {
        closePopX();
    }
});