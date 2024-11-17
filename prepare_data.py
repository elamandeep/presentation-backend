from app import ProvinceItems, db, app as flaskApp


province_items_data = [
    ProvinceItems(
        province_id=1,
        item_name="Mount Everest",
        img_url="https://res.cloudinary.com/duskdho4x/image/upload/v1731856480/provinces/r34r6cwb7vwkimnootm5.jpg",
    ),
    ProvinceItems(
        province_id=1,
        item_name="Kanchenjunga",
        img_url="https://res.cloudinary.com/duskdho4x/image/upload/v1731856480/provinces/a29t5q7bcjdtq48fck6o.jpg",
    ),
    ProvinceItems(
        province_id=1,
        item_name="Sagarmatha National Park",
        img_url="https://res.cloudinary.com/duskdho4x/image/upload/v1731856480/provinces/jgioyhzvvtsf0d5uyuxp.jpg",
    ),
    ProvinceItems(
        province_id=1,
        item_name="Pashupatinath Temple",
        img_url="https://res.cloudinary.com/duskdho4x/image/upload/v1731856479/provinces/zwu3jnvs1lqjey80bz0l.jpg",
    ),
    ProvinceItems(
        province_id=2,
        item_name="Janaki Mandir",
        img_url="https://res.cloudinary.com/duskdho4x/image/upload/v1731856479/provinces/slbrbwg5krfdsqshjhlx.jpg",
    ),
    ProvinceItems(
        province_id=2,
        item_name="Parsa Wildlife Reserve",
        img_url="https://res.cloudinary.com/duskdho4x/image/upload/v1731856478/provinces/mjzfmznjfbuyk6ousnik.jpg",
    ),
    ProvinceItems(
        province_id=3,
        item_name="Boudhanath Stupa",
        img_url="https://res.cloudinary.com/duskdho4x/image/upload/v1731856478/provinces/znlce8nfb7rzvwsxuw8y.jpg",
    ),
    ProvinceItems(
        province_id=3,
        item_name="Kathmandu Valley",
        img_url="https://res.cloudinary.com/duskdho4x/image/upload/v1731856478/provinces/xjw1vrkziudd9gwnu4sa.jpg",
    ),
    ProvinceItems(
        province_id=3,
        item_name="Swayambhunath Stupa",
        img_url="https://res.cloudinary.com/duskdho4x/image/upload/v1731856477/provinces/ch5yfdvhsdlzpbklt1nm.jpg",
    ),
    ProvinceItems(
        province_id=3,
        item_name="Chitwan National Park",
        img_url="https://res.cloudinary.com/duskdho4x/image/upload/v1731856477/provinces/j4n3d1nu3lfewduulx8z.jpg",
    ),
    ProvinceItems(
        province_id=4,
        item_name="Pokhara",
        img_url="https://res.cloudinary.com/duskdho4x/image/upload/v1731856477/provinces/ot2m4e4oithaunsklh8e.jpg",
    ),
    ProvinceItems(
        province_id=4,
        item_name="Annapurna Circuit Trek",
        img_url="https://res.cloudinary.com/duskdho4x/image/upload/v1731856477/provinces/fspjksykm8psmbudncu0.jpg",
    ),
    ProvinceItems(
        province_id=4,
        item_name="Manakamana Temple",
        img_url="https://res.cloudinary.com/duskdho4x/image/upload/v1731856476/provinces/ygbwpzfndqx8shnfpbjo.jpg",
    ),
    ProvinceItems(
        province_id=4,
        item_name="Gorkha",
        img_url="https://res.cloudinary.com/duskdho4x/image/upload/v1731856476/provinces/edc1oqpx2lfwgse0psqk.jpg",
    ),
    ProvinceItems(
        province_id=5,
        item_name="Lumbini",
        img_url="https://res.cloudinary.com/duskdho4x/image/upload/v1731856476/provinces/cc0c25uzq0tugwmclnoa.jpg",
    ),
    ProvinceItems(
        province_id=5,
        item_name="Tilaurakot",
        img_url="https://res.cloudinary.com/duskdho4x/image/upload/v1731856475/provinces/z1kgs7egkbqz4svljdre.jpg",
    ),
    ProvinceItems(
        province_id=5,
        item_name="Kapilvastu",
        img_url="https://res.cloudinary.com/duskdho4x/image/upload/v1731856463/provinces/qz2kreyesfzuuwneivzn.jpg",
    ),
    ProvinceItems(
        province_id=5,
        item_name="Dang",
        img_url="https://res.cloudinary.com/duskdho4x/image/upload/v1731856463/provinces/bqg1wqjcn0rwfpficati.jpg",
    ),
    ProvinceItems(
        province_id=6,
        item_name="Khaptad National Park",
        img_url="https://res.cloudinary.com/duskdho4x/image/upload/v1731856464/provinces/ut5ewpxy5wzxsbehdpx7.jpg",
    ),
    ProvinceItems(
        province_id=6,
        item_name="Shuklaphanta National Park",
        img_url="https://res.cloudinary.com/duskdho4x/image/upload/v1731856464/provinces/q8tkb4btevugp4za6wn0.jpg",
    ),
    ProvinceItems(
        province_id=6,
        item_name="Mahendranagar",
        img_url="https://res.cloudinary.com/duskdho4x/image/upload/v1731856463/provinces/onsjjij4ay4cwoldy9yk.jpg",
    ),
    ProvinceItems(
        province_id=6,
        item_name="Baitadi",
        img_url="https://res.cloudinary.com/duskdho4x/image/upload/v1731856463/provinces/qtjofdqdnrgmrz864pqq.jpg",
    ),
    ProvinceItems(
        province_id=7,
        item_name="Rara Lake",
        img_url="https://res.cloudinary.com/duskdho4x/image/upload/v1731856462/provinces/ajmykxp7ibceoeemvjyf.jpg",
    ),
    ProvinceItems(
        province_id=7,
        item_name="Shey-Phoksundo National Park",
        img_url="https://res.cloudinary.com/duskdho4x/image/upload/v1731856463/provinces/m0aqdbjjlqvdbdgq0tfy.jpg",
    ),
    ProvinceItems(
        province_id=7,
        item_name="Humla",
        img_url="https://res.cloudinary.com/duskdho4x/image/upload/v1731856462/provinces/cohafqfenhzs7unezo4r.jpg",
    ),
    ProvinceItems(
        province_id=7,
        item_name="Dolpa",
        img_url="https://res.cloudinary.com/duskdho4x/image/upload/v1731856463/provinces/afclcdijsh7lkuanmdhd.jpg",
    ),
]


def prepare():
    db.session.bulk_save_objects(province_items_data)
    db.session.commit()
    db.session.close()


if __name__ == "__main__":
    with flaskApp.app_context():
        prepare()
        print("data prepared successfully")
