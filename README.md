一道有趣的同步题：

1. 有一个线程持续打印'<'
2. 有一个线程持续打印'>'
3. 有一个线程持续打印'_'
4. 同步这三个进程，使打印结果总是完整的小鱼: `<><` 或 `><>` , 用 `_` 进行分割

求解思路：想象成状态机