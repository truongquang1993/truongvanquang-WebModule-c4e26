from EX1 import db

# 1. select collection
post_collection = db["posts"]

# 2. Create a new post
new_post = {
    "title": "Nếu biết trăm năm là hữu hạn",
    "author": "Phạm Lữ Ân",
    "content": "Người ta gọi tuổi mới lớn là 'tuổi biết buồn'. 'Biết buồn' tức là chạm ngõ cuộc đời rồi đó. Biết buồn tức là bắt đầu nhận ra sự hiện hữu của những khoảng trống trong tâm hồn. Biết buồn là khi nhận ra rằng có những lúc mình cảm thấy cô độc. Khi đó, hãy dành cho sự cô độc một khoảng riêng, hãy đóng khung sự cô đơn trong giới hạn của nó, như một căn phòng trống trong ngôi nhà tâm hồn. Mỗi lần vào căn phòng ấy, dù tự nguyện hay bị xô đẩy, thì bạn vẫn có thể điềm tĩnh khám phá bản thân trong sự tĩnh lặng. Để rồi sau đó, bạn bình thản bước ra, khép cánh cửa lại và trở về với cuộc sống bề bộn thường ngày, vốn lắm nỗi buồn nhưng cũng không bao giờ thiếu niềm vui..."
}# document

# 3. Insert new document into collection
post_collection.insert_one(new_post)

