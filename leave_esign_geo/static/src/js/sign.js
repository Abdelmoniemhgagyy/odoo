///** @odoo-module **/
//
//import { jsonRpc } from "@web/core/network/rpc_service";
//
//document.addEventListener('DOMContentLoaded', () => {
//    const canvas = document.getElementById('signature-pad');
//    if (!canvas) return;
//
//    const ctx = canvas.getContext('2d');
//
//    // ✅ أضفنا styling للـ pen
//    ctx.strokeStyle = '#000000';
//    ctx.lineWidth = 2;
//    ctx.lineCap = 'round';
//    ctx.lineJoin = 'round';
//
//    let drawing = false;
//    let rect = canvas.getBoundingClientRect();
//
//    const resizeRect = () => rect = canvas.getBoundingClientRect();
//    window.addEventListener('resize', resizeRect);
//
//    const start = (e) => {
//        drawing = true;
//        ctx.beginPath();
//        ctx.moveTo(e.clientX - rect.left, e.clientY - rect.top);
//    };
//
//    const draw = (e) => {
//        if (!drawing) return;
//        ctx.lineTo(e.clientX - rect.left, e.clientY - rect.top);
//        ctx.stroke();
//    };
//
//    const end = () => {
//        drawing = false;
//        ctx.closePath();
//    };
//
//    canvas.addEventListener('mousedown', start);
//    canvas.addEventListener('mousemove', draw);
//    window.addEventListener('mouseup', end);
//    canvas.addEventListener('mouseout', end);
//
//    // ✅ Clear button
//    const clearBtn = document.getElementById('clear-sign');
//    if (clearBtn) {
//        clearBtn.addEventListener('click', () => {
//            ctx.clearRect(0, 0, canvas.width, canvas.height);
//        });
//    }
//
//    // ✅ Submit button
//    const submitBtn = document.getElementById('submit-sign');
//    if (submitBtn) {
//        submitBtn.addEventListener('click', async () => {
//            const data = canvas.toDataURL('image/png');
//            const token = document.getElementById('leave-token').value;
//            const status = document.getElementById('sign-status');
//            status.innerText = 'جاري جمع الموقع...';
//
//            const send = async (lat, lon) => {
//                status.innerText = 'جاري إرسال التوقيع...';
//                try {
//                    const res = await jsonRpc('/leave/sign/submit', 'call', {
//                        token,
//                        signature_data: data,
//                        lat,
//                        lon
//                    });
//                    status.innerText = res.success ? '✓ تم التوقيع بنجاح. شكراً' : '✗ خطأ: ' + (res.error || 'غير معروف');
//                    if (res.success) {
//                        submitBtn.disabled = true;
//                        clearBtn.disabled = true;
//                    }
//                } catch (err) {
//                    status.innerText = '✗ خطأ: ' + err.message;
//                    console.error('Error:', err);
//                }
//            };
//
//            if (navigator.geolocation) {
//                navigator.geolocation.getCurrentPosition(
//                    pos => send(pos.coords.latitude, pos.coords.longitude),
//                    () => send('', '')
//                );
//            } else {
//                send('', '');
//            }
//        });
//    }
//});