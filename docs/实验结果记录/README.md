# 实验结果记录

## IMSI 抓取攻击

### 1 攻击原理

IMSI 抓取攻击可以分为 2 种：

- 被动抓取：通过 `attach_request` 消息的 nas 数据抓取 UE 的 IMSI
- 主动抓取：通过主动向 UE 发起 `identity_request` 消息抓取 UE 的 IMSI

### 2 攻击效果

被动抓取的抓包结果如下：

![image-20230503190814065](images/image-20230503190814065.png)

主动抓取的抓包结果如下：

![image-20230503190828019](images/image-20230503190828019.png)

## 麻木攻击

### 1 攻击原理

当 UE 进行 attach 时，在 MME 接收到相应的 nas 数据后，不发送 `authentication_request` 消息，而是直接回复一条 `authentication_reject` 消息。

该 `authentication_reject` 消息是明文，没有进行加密和完整性保护，因此该攻击在真实环境中是可能被实现的。

### 2 攻击效果

UE 进入无服务（麻木）状态（`user-inactivity`），除非重启或者重新插入 USIM 卡，否则将无法再附着到 EPC 中。

跳过该处插桩点，继续协议栈原流程，MME 发送一条 `authentication_request` 消息，UE 不再有任何响应。

抓包结果如下：

![image-20230503191049790](images/image-20230503191049790.png)

UE 状态变化：

![image-20230503191105061](images/image-20230503191105061.png)

## 鉴权同步失败攻击

### 1 攻击原理

当 UE 向 EPC 发起附着后，在 MME 开始处理受害者 UE 的 `attach_request` 消息之前，可以在客户端使用受害者 UE 的 IMSI 伪造多条具有不同安全能力的 `attach_request` 消息并发送到 MME，增加 HSS 中对应 IMSI 的 sqn 值并使之与 UE 中的 sqn 值的差值超过可以同步的范围。

### 2 攻击效果

当受害者 UE 正常进行附着，MME 发起鉴权请求后，在 UE 处会鉴权失败，UE 向 MME 回复一条 `authentication_failure` 消息，该消息中携带有 UE 当前的 sqn 值，可以使 HSS 与 UE 重新达成同步。

鉴权失败后，MME 会重新进行鉴权流程，向 UE 发送鉴权请求，之后 UE 还是可以正常接入 EPC。

抓包结果如下：

![image-20230503191302148](images/image-20230503191302148.png)

## 悄然中断攻击

### 1 攻击原理

网络向 UE 发送一条使用 IMSI 作为 UE id 的寻呼消息，使 UE 与其原网络进行分离，并向当前网络（伪基站）进行附着。

> 暂未在本平台上验证该攻击。

## 分离降级攻击

### 1 攻击原理

网络向 UE 发送一条 `detach_request` 消息，使 UE 从网络断开连接，并使 UE 向其回复一条 `detach_accept` 消息。

该 `detach_request` 消息是经过加密和完整性保护的，在实际环境中可行吗？

```c++
// srsRAN 中 detach_request 的消息结构
typedef struct {
LIBLTE_MME_DETACH_TYPE_STRUCT detach_type;
LIBLTE_MME_NAS_KEY_SET_ID_STRUCT nas_ksi;
LIBLTE_MME_EPS_MOBILE_ID_STRUCT eps_mobile_id;
} LIBLTE_MME_DETACH_REQUEST_MSG_STRUCT;
```

> 参考资料：TS 24.301, Sec 5.5.2.2.1, UE initiated detach request

### 2 攻击效果

在论文中 UE 对不同类型的 `detach_request` 消息的反应如下：

![image-20230503191554660](images/image-20230503191554660.png)

srsRAN 的代码实现：

```c++
// srsRAN 中 detach_request 的消息类型
typedef struct {
uint8 switch_off;
uint8 type_of_detach;
} LIBLTE_MME_DETACH_TYPE_STRUCT;
```

> 参考资料：24.301 v10.2.0 Section 9.9.3.7

实际实验结果：

UE 回复一条 `detach_accept` 消息，并断开与网络的连接，显示“无服务”状。接着 MME 会释放 UE 的上下文。

一段时间后 UE 会重新发起 attach 流程，并重新接入核心网中。实验结果说明了该攻击可以造成短暂的拒绝服务攻击，可以降低用户的使用体验，并在某些紧急情况（如：抢险抗灾）下影响任务的执行。

抓包结果如下：

![image-20230503191658808](images/image-20230503191658808.png)

## 拒绝服务攻击（attach_reject）

### 1 攻击原理

当 UE 发起附着后，直接回复一条 `attach_reject` 消息。

### 2 攻击效果

这条 `attach_reject` 消息会使 UE 进入不可用状态，UE 被禁止接入 4G 网络，显示“无服务”状态，直到 UE 重启。

抓包结果如下：

![image-20230503191812315](images/image-20230503191812315.png)

