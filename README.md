# phonenap-legal

Trang web của PhoneNap trên GitHub Pages: homepage, Privacy Policy, Support và Terms of Use. Đây là các link điền vào App Store Connect.

- Homepage: https://datnntqn.github.io/phonenap-legal/
- Privacy: https://datnntqn.github.io/phonenap-legal/privacy.html
- Support: https://datnntqn.github.io/phonenap-legal/support.html
- Terms: https://datnntqn.github.io/phonenap-legal/terms.html

## Cấu trúc
- `index.html`, `privacy.html`, `support.html`, `terms.html`: HTML tĩnh, không cần build.
- `assets/site.css`: style chung (màu, font và chuyển động theo bước giống app).
- `assets/site.js`: link App Store cho mọi nút tải. Điền `APP_STORE_URL` khi app đã lên App Store; khi còn trống, nút hiện "Coming soon".
- `assets/sprites/`: sprite SVG nền trong suốt, sinh từ `SpriteCatalog` của app.
- `assets/shots/`: ảnh màn hình lấy từ snapshot test của app.

## Việc thường làm
- Vẽ lại sprite trong app: `python3 scripts/sprites-to-svg.py ../pixelpet/Packages/PixelPetKit/Sources/DesignSystem assets/sprites`
- Xem thử trên máy: `python3 -m http.server 8000` rồi mở http://localhost:8000. Muốn xem trên iPhone (cùng Wi‑Fi) thì thêm `--bind 0.0.0.0` và mở địa chỉ IP của Mac.
- Khi app lên App Store: điền `APP_STORE_URL` trong `assets/site.js`, và bỏ comment dòng `apple-itunes-app` trong `index.html` (điền app id) để Safari hiện Smart App Banner.

## Bật GitHub Pages
Settings › Pages › Deploy from a branch › `main` / `(root)`.
