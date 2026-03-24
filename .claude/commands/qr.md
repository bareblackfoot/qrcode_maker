URL을 받아 기본 흑백 QR 코드를 생성하고 클립보드에 복사합니다.

사용법: /qr <URL>

## 수행할 작업

1. 아래 Python 코드를 실행하여 QR 코드를 생성합니다:

```python
import qrcode
img = qrcode.make('$ARGUMENTS')
img.save('QR_output.png')
```

2. 생성된 QR 이미지를 클립보드에 복사합니다:

```powershell
powershell -Command "Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.Clipboard]::SetImage([System.Drawing.Image]::FromFile('QR_output.png'))"
```

3. 생성된 QR 코드 이미지를 사용자에게 보여줍니다.

4. 완료 후 사용자에게 클립보드에 복사되었음을 알립니다.
