window.nitroAds = window.nitroAds || {
  createAd: function () {
    return new Promise((e) => {
      window.nitroAds.queue.push(['createAd', arguments, e]);
    });
  },
  addUserToken: function () {
    window.nitroAds.queue.push(['addUserToken', arguments]);
  },
  queue: [],
};

var script = document.createElement('script');
script.src = 'https://s.nitropay.com/ads-1843.js';
script.setAttribute('data-cfasync', 'false');
script.async = true;
document.head.appendChild(script);

function npCreateAds(adsArray) {
  const sizeMappings = {
    largeleaderboard: [
      ['728', '90'],
      ['970', '90'],
      ['970', '250'],
    ],
    leaderboard: [['728', '90']],
    hpu: [
      ['300', '250'],
      ['120', '600'],
      ['160', '600'],
      ['300', '600'],
    ],
    mpu: [
      ['300', '250'],
      ['250', '250'],
    ],
    rectangle: [
      ['300', '250'],
      ['250', '250'],
      ['336', '280'],
    ],
    sky: [
      ['120', '600'],
      ['160', '600'],
    ],
    mobile_leaderboard: [['320', '50']],
  };

  adsArray.forEach((ad) => {
    let allowedSizes = sizeMappings[ad.size] || [];
    let adOptions = {
      sizes: allowedSizes,
      refreshLimit: 0,
      refreshTime: 30,
      renderVisibleOnly: false,
      refreshVisibleOnly: true,
      delayLoading: false,
    };
    if (ad.size === 'mobile_leaderboard') {
      adOptions.mediaQuery = '(min-width: 320px) and (max-width: 767px)';
    }

    if (window['nitroAds']) {
      window['nitroAds'].createAd(ad.divId, adOptions);
    } else {
      console.error('nitroAds is not defined.');
    }
  });
}

window.npCreateAds = npCreateAds;
