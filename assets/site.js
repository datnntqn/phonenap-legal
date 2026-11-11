// The App Store link for every "Get" and "Download" button. Empty = buttons show "Coming soon".
const APP_STORE_URL = 'https://apps.apple.com/us/app/phonenap-screen-time-blocker/id6829627663';

document.querySelectorAll('[data-appstore]').forEach((a) => {
  if (APP_STORE_URL) {
    a.href = APP_STORE_URL;
  } else {
    a.removeAttribute('href');
    a.setAttribute('aria-disabled', 'true');
    a.textContent = a.dataset.soon || 'Coming soon';
  }
});
