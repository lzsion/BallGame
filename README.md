# Ball Game弹球小游戏

## 前言

此项目是简单的弹球小游戏，游戏的创意灵感来源于游戏[Pummel Party](https://store.steampowered.com/app/880940/Pummel_Party/)中的一款多人弹球游戏，这里只做了2个玩家，较为简陋。

此程序使用python语言编写，调用了pygame库。

项目程序已封装至

> ./dist/main/BallGame.exe

## 游戏演示

游戏开始界面如下图，可以选择电脑玩家进行对战，也可以本地两个玩家进行对战。选择结束后按下空格进行游戏，游戏前有三秒准备时间。

![BallGame_1](https://lzs-imgs.oss-cn-hangzhou.aliyuncs.com/ball-game/BallGame_1.png)

游戏进行过程如下图，球从中间发出，方向和速度随机，初始球为白色，不属于任何一方。

玩家操作左右两边的板块上下移动击球，击中的球会显示为己方颜色，若对方未接中己方的球则己方得分，若己方未接中对方的球则对方得分，白球不计分。

画面中上方为双方得分和剩余时间，设定一局游戏为60秒，时间到则游戏结束。

板子轨道上的小点为预计球的落点，原先为方便分析电脑操作的合理性，后为方便进行游戏保留。

![BallGame_2](https://lzs-imgs.oss-cn-hangzhou.aliyuncs.com/ball-game/BallGame_2.png)

游戏结束界面如下图，游戏结束界面显示谁是胜者，得分相同时会显示平局，按下'r'键重新开始。

![BallGame_3](https://lzs-imgs.oss-cn-hangzhou.aliyuncs.com/ball-game/BallGame_3.png)
