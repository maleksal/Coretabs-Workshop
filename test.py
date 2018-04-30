from shop.models import Category,Product
c1 = Category(name="Mobile Devices")
c1.save()
c2 = Category(name="Computers")
c2.save()
p1 = Product(
        name="Apple iPhone X",
        price=1149.99,
        stock=12,
        description="iPhone X features a new all-screen design. FaceID, which makes your face your password. And the most powerful and smartest chip ever in a smartphone.",
        category=c1)
p1.save()
p2 = Product(
        name="Google Pixel2",
        price=860.20,
        stock=14,
        description="The unlocked Pixel 2 provides a clean, bloat-free experience with no unwanted apps, one of the highest rated smartphone cameras, with free unlimited storage.",
        category=c1)
p2.save()
p3 = Product(
        name="Sony Xperia ZX2",
        price=920.49,
        stock=9,
        description="The Xperia XZ2 is packed with the latest Sony technologies to deliver an entertainment experience that touches your senses in a whole new way – whether you’re lost in a HDR movie or capturing hidden details with the new advanced Motion Eye™ camera.",
        category=c1)
p3.save()
p4 = Product(
        name="Dell Inspiron 175000",
        price=799.99,
        stock=11,
        description="17-inch laptop with an anti-glare, backlit display. Add options like an FHD screen with discrete graphics to create a PC that reflects what matters to you.",
        category=c2)
p4.save()
p5 = Product(
        name="Macbook Pro",
        price=29999.00,
        stock=162,
        description="It’s razor thin, feather light, and even faster and more powerful than before. It has the brightest, most colorful Mac notebook display ever. And it features the Touch Bar — a Multi-Touch enabled strip of glass built into the keyboard for instant access to the tools you want, right when you want them. MacBook Pro is built on groundbreaking ideas. And it’s ready for yours.",
        category=c2)
p5.save()

