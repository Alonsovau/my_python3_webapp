import www.orm,asyncio
from www.models import User,Blog,Comment

# async def test():
#     await www.orm.create_pool(loop=loop,user='root',password='password',database='awesome')
#     u=User(name='Test',email='test@example.com',passwd='1234567890',image='about:blank')
#     await u.save()
#
#
# loop=asyncio.get_event_loop()
# loop.run_until_complete(test())
# loop.close()