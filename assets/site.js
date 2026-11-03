// The App Store link for every "Get" and "Download" button. Fill in once the app is live.
const APP_STORE_URL = '';

document.querySelectorAll('[data-appstore]').forEach((a) => {
  if (APP_STORE_URL) {
    a.href = APP_STORE_URL;
  } else {
    a.removeAttribute('href');
    a.setAttribute('aria-disabled', 'true');
    a.textContent = a.dataset.soon || 'Coming soon';
  }
});
