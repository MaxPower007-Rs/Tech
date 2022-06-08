# MQTT
## By [Naveen PS](https://www.linkedin.com/posts/naveenpsofficial_mqtt-iot-packet-activity-6939899955394285568-hLJu/?utm_source=linkedin_share&utm_medium=member_desktop_web)

Contribution Naveen PS
MQTT is Message Queuing Telemetry Transport Right? - NO! WRONG!

It's Simply

MQ Telemetry Transport

The MQ is in reference to a product called IBM MQ.

I will be posting MQTT related concepts and their practical use cases for next few days. Follow my LinkedIn profile to get updates.
#mqtt #iot

𝑴𝑸𝑻𝑻 𝑰𝒏𝒔𝒊𝒈𝒉𝒕𝒔 : 1

We got MQTT 5 after MQTT 3.1.1. What happened to MQTT 4?!

The answer lies hidden inside the Variable Header part of the MQTT CONNECT Packet.

To be exact, we need to examine an 8 bit unsigned value that represents the version shown in the below picture.
For MQTT 3.1 - this is 0x03
For MQTT 3.1.1 -  this is 0x04 
Thus MQTT 3.1.1 was actually the 4th version of MQTT.

So the answer is:
To avoid unnecessary confusion the specification group agreed to name the next MQTT version, as version 5 because the value was 0x05.

This is Post 2 of my 𝑴𝑸𝑻𝑻 𝑰𝒏𝒔𝒊𝒈𝒉𝒕𝒔 Series.

Do check it out: More MQTT Insights are coming daily for the next week.
#mqtt #iot #wireshark #packet

![image](https://user-images.githubusercontent.com/56212392/172646440-f9462038-a2e9-4b0d-89a0-e9a6a436a026.png)

We explain MQTT in terms of publishers & subscribers. Instead, we should always understand & implement in terms of Clients & the Broker. Why?

A Client can be a publisher & subscriber at the same time!

By teaching/learning in terms of publishers & subscribers, we are unnecessarily complicating things. 

Thus, in the same client code, we can use functions to publish and subscribe to topics.

Example Scenario: 
Imagine a fleet of sensors in a factory all publishing real time values to an MQTT Broker. An Edge Compute Device subscribes to all the topics to which these sensors are publishing to. It uses ML for predictive maintenance. When an event is predicted, the Edge Compute Device will publish to a new topic for notifying the maintenance crew. The Dashboard Client of the Maintenance Crew will get an alert as it is subscribed to this topic. Thus, the Edge Compute Device acts both as a publisher and a subscriber. 

This is Post 3 of my 𝑴𝑸𝑻𝑻 𝑰𝒏𝒔𝒊𝒈𝒉𝒕𝒔 Series.

A Last Will & Testament is a legal document used to transfer assets to beneficiaries after death. MQTT also has a Last Will & Testament feature! Curious?!

Imagine that you have deployed hundreds of sensor nodes across a factory in hard-to-reach places. Essentially, it's hard to debug or diagnose manually. Now, say, around half a dozen of the sensor nodes over a period of a week disconnects ungracefully or are non-responsive. If you have not implemented the Last Will & Testament Feature (LWT) it will be a pain to pinpoint the exact sensors that are non-responsive.

How will LWT help in such a situation?

When a client first connects to the broker, each client can specify its last will message and corresponding last will topic to which this last will message needs to be published in case of an "ungraceful" disconnect due to network outage, battery issue, or any physical damage.

Whenever a Client establishes the first connection with the broker, it uses the MQTT CONNECT Packet. While many learn that this packet does not have any message details, it's technically wrong. We can actually send the LWT Message and Topic using the CONNECT Packet.

So you might be asking what happens next?

Now the Broker will store the LWT Message & the topic to publish. When any of the following conditions happen the broker publishes the saved LWT Message to the LWT Topic:
1.The broker detects a network failure.
2.The client does not send a DISCONNECT packet before it closes the connection.
3.The broker closes the network because of a protocol error.

So in the Factory Scenario, say we have configured all sensors to publish its own sensor ID or location to say a LWT topic called /failedsensor/.

A Dashboard Client can subscribe to /failedsensor/ topic and when any sensor disconnects we will get sensor ID or location in this common topic to collect this specific detail. Thus we can pinpoint the exact sensor node which is misbehaving.

This is Post 4 of my 𝑴𝑸𝑻𝑻 𝑰𝒏𝒔𝒊𝒈𝒉𝒕𝒔 Series.

![image](https://user-images.githubusercontent.com/56212392/172646716-ee1e51fb-bb9c-4f27-9c69-238c720ca8e7.png)

MQTT provides Level 2 QoS to ensure that a message is sent exactly once - no duplicates, no loss. So you publish with QoS 2, but still the subscriber client receives messages unreliably! Why? Understanding this is very important for mission-critical applications.

Before we go into why this happened, let's clarify the Quality of Service levels in MQTT.

There are 3 QoS levels in MQTT:
QoS 0 - Message may reach at most once - dropped packages are common
QoS 1 - Message will reach at least once - but duplicates can happen
QoS 2 - Message will reach exactly once - acknowledgments make sure this happens

Now coming back to the problem at hand, why did the subscriber client get the message in the unreliable QoS 0 or 1 while we published in QoS 2?

This is because we didn't look at the two sides of the message delivery as separate events from the perspective of the broker! - Remember subscriber clients are isolated from publisher clients by the broker.

Thus just like Publishing QoS Level, there is Subscribing QoS Level also.

So the solution is to modify the subscriber client code, to accept messages from broker with QoS level 2 only.

So in Short, the broker downgrades the QoS level to default QoS level expected by the subscriber client as it was not specifically set from the subscriber client side.

Key Takeaway: Set Subscriber QoS level also. It should match the Publish QoS level for optimum performance as expected.

This is Post 5 of my 𝑴𝑸𝑻𝑻 𝑰𝒏𝒔𝒊𝒈𝒉𝒕𝒔 Series.

MQTT provides Level 2 QoS to ensure that a message is sent exactly once - no duplicates, no loss. So you publish with QoS 2, but still the subscriber client receives messages unreliably! Why? Understanding this is very important for mission-critical applications.

Before we go into why this happened, let's clarify the Quality of Service levels in MQTT.

There are 3 QoS levels in MQTT:
QoS 0 - Message may reach at most once - dropped packages are common
QoS 1 - Message will reach at least once - but duplicates can happen
QoS 2 - Message will reach exactly once - acknowledgments make sure this happens

Now coming back to the problem at hand, why did the subscriber client get the message in the unreliable QoS 0 or 1 while we published in QoS 2?

This is because we didn't look at the two sides of the message delivery as separate events from the perspective of the broker! - Remember subscriber clients are isolated from publisher clients by the broker.

Thus just like Publishing QoS Level, there is Subscribing QoS Level also.

So the solution is to modify the subscriber client code, to accept messages from broker with QoS level 2 only.

So in Short, the broker downgrades the QoS level to default QoS level expected by the subscriber client as it was not specifically set from the subscriber client side.

Key Takeaway: Set Subscriber QoS level also. It should match the Publish QoS level for optimum performance as expected.

This is Post 5 of my 𝑴𝑸𝑻𝑻 𝑰𝒏𝒔𝒊𝒈𝒉𝒕𝒔 Series.

![image](https://user-images.githubusercontent.com/56212392/172646867-4ca54102-59f2-4408-93d1-a98275b4b20f.png)

QoS 0 in MQTT doesn’t guarantee message delivery. QoS 1 guarantees but duplicate messages are frequent. So QoS 2 is the best right? Not necessarily.

It depends on the application. Choosing the right MQTT QoS Level for your subscriber and publisher clients is very important. 

QoS Level 0 is “fire & forget” meaning 1 single publish packet is send
QoS Level 1 uses 2 packets. One to publish and one PUBACK for acknowledgment 
QoS Level 2 uses a whopping 4 packets - 2 extra for Mutual Acknowledgement and 1 more to complete the transaction 

So When to use which QoS in MQTT?

QoS 0:
No message queuing needed (broker is not advanced/capable)
Completely Stable Connection (wired)
Loss of some messages is acceptable (not mission critical)
Fastest & Realtime messaging

QoS 1:
You can’t bear the overhead of QoS 2 
Application able to tolerate duplicates or filter them out
All messages must reach the subscriber but not time critical

QoS 2:
Mission Critical Application
No tolerance for false readings
Overhead is justifiable due to the importance of the application

Most people will be OK with QoS 1. It strikes the right balance.

Note:
MQTT is an application layer protocol on top of TCP/IP. What many people forget is that TCP employs its own error connection and each TCP/IP packet is acknowledged. MQTT is an application level protocol and an application message can result in multiple TCP/IP packets.

So Whenever you implement an MQTT based system, use a Packet Sniffer and a Packet Analyser like Wireshark to analyze and optimize your system.

This is Post 6 of my 𝑴𝑸𝑻𝑻 𝑰𝒏𝒔𝒊𝒈𝒉𝒕𝒔 Series.

![image](https://user-images.githubusercontent.com/56212392/172646960-80e1bbc3-c7b3-405b-8b88-fac384296786.png)

What happens if a Subscriber is disconnected from the Broker while the Publisher is sending an important Message, Like GPS data, Distress Signal? Is the message lost? 

MQTT has a trick up its sleeve for such situations.

Remember MQTT is not a Queuing system by design like many misunderstand, but we do have a feature to explicitly make the Broker remember the Last Retained Message for that particular topic.

The feature is called Retained Messages.

When you publish any messages to a topic inside a broker, we can set the Retain Flag to 1 in the packet headers. Retained messages help newly-subscribed clients get a status update immediately after they subscribe to a topic. The retained message eliminates the wait for the publishing clients to send the next update.

Thus it is very useful for clients that send data in intervals like temperature readings, GPS coordinates, and other data. Without retained messages, new subscribers are kept in the dark between publish intervals.

Important Note: Once a retained message is set, don't forget to delete it or update it once its usage is over. Not doing this will create confusion for subscriber clients when it seemingly receives the retained message instead of real time message.

So how to delete retained messages?

You just need to send a zero-byte payload message with the retain flag set to1 on the topic where you want to delete the previous retained message. 

This is Post 7 of my 𝑴𝑸𝑻𝑻 𝑰𝒏𝒔𝒊𝒈𝒉𝒕𝒔 Series.

![image](https://user-images.githubusercontent.com/56212392/172647067-ccac5ae5-998d-46e8-914f-96a8f1567b50.png)

1000s of publishers & 1000s of topics. Will you be manually subscribing to each topic in the Sub Client Code? MQTT has a trick up its sleeve to sub to multiple topics with just a single line of code or single packet.

MQTT uses the concept of Wildcards to do this. 

Remember that a wildcard can only be used to subscribe to multiple topics at the same time and not publish.

There are two different kinds of wildcards: 
Single-level - Represented by "+"
Multi-level - Represented by "#"

First Look at the Image Below. This is a sample topic pattern in broker to explain these wildcards.

Single Level: A single-level wildcard replaces one topic level. Any topic matches a topic with a single-level wildcard if it contains an arbitrary string instead of the wildcard. 

Multi-level: When a client subscribes to a topic with a multi-level wildcard, it receives all messages for a topic that begin with the pattern before the wildcard character, no matter how long or deep the topic is. The multi-level wildcard must be placed as the last character in the topic and preceded by a forward slash.

Combining "+" & "#" - Yes, this is possible too. You can use both wildcards in a single subscription call to do granular filtering of topics, to exactly sub to the topics that we want for a scenario. 

This is Post 8 of my 𝑴𝑸𝑻𝑻 𝑰𝒏𝒔𝒊𝒈𝒉𝒕𝒔 Series. 

![image](https://user-images.githubusercontent.com/56212392/172645784-f486a09b-2522-4059-a343-e8ca88decd86.png)

When Connection between a Client & Broker in MQTT disconnects the topics are lost and the client needs to subscribe again on reconnect. This is so inefficient. MQTT developers often fail to consider such situations, which are common in resource-constrained applications.

MQTT provides a feature called Persistent sessions for such situations. 

How to enabled Persistent session?

When a client connects to the broker, it can request a persistent session, by setting the cleanSession flag to false in the initial CONNECT Packet.

Only in this situation, the broker is allowed to store/queue that specific client information. This is why MQTT is not  "Message Queueing"  by default.

So, now you have enabled persistent session for a specific client. What all things are now stored in the broker for this specific client for the session to Persist?

When the client reconnects, these information are available immediately.
1.Existence of a session (even if there are no subscriptions).
2.All the subscriptions of the client.
3.All messages in a Quality of Service (QoS) 1 or 2 flow that the client has not yet confirmed.
4.All new QoS 1 or 2 messages that the client missed while offline.
5.All QoS 2 messages received from the client that are not yet completely acknowledged.

You might have some questions now. Let me answer them.

1. How long does the broker store messages? 
Until the client comes back online and receives the message, or until the memory limit of the Broker is achieved.

2. How does a reconnected client know if a session is already stored?
The connection acknowledgement packet called CONNACK  from the broker contains a session present flag. This flag tells the client if a previously established session is still available on the broker.

![image](https://user-images.githubusercontent.com/56212392/172646010-fc339091-fed4-4f66-b983-0b78ca080d20.png)

Unlike Software, Security breaches in IoT can literally harm real people. If MQTT is implemented, then make sure to properly use & implement the Security Features in it.

As MQTT is an Application Protocol built on top of TCP/IP, all Network Level and Transport Level Security is the same as any TCP/IP Application. On the application level MQTT provides many Security Features.

Let's do an overview, so that you understand the flexibility and depth of Security in MQTT.

AUTHENTICATION:
1. MQTT authentication with Username + Password - but these are present as plain text on the CONNECT Packet

2. MQTT Authentication with Username + Password + Unique Client ID

3. Message Data Integrity Check - MQTT PUBLISH packets can contain Checksum that verifies the contents of the packet haven't been tampered with.

AUTHORIZATION:
1. This is configured in the Broker. It has the following control over what a Client is allowed to do
   a.Allowed topic
   b.Allowed operation - publish, subscribe, both
   c.Allowed QoS level (0, 1, 2, all)

2. OAuth 2.0-based Authentication - Allows a client to access a resource that is owned by a resource owner without giving unencrypted credentials to the client

ENCRYPTION:
1. Transport Layer Encryption with TLS/SSL
2. MQTT Payload Encryption on top of  TLS/SSL
3. X509 Client Certificate Based Security


This is Post 10 of my 𝑴𝑸𝑻𝑻 𝑰𝒏𝒔𝒊𝒈𝒉𝒕𝒔 Series. Previous Posts can be found below:
1. https://lnkd.in/d9uCZUcU
2. https://lnkd.in/dcwnM435
3. https://lnkd.in/d7rSkw_M
4. https://lnkd.in/dsFP59vd
5. https://lnkd.in/dEHfQfQe
6. https://lnkd.in/dercVDTp
7. https://lnkd.in/d8Z3H734
8. https://lnkd.in/dvd9tyiC
9. https://lnkd.in/dQSYPNx8

I have published 10 MQTT Posts over the last few weeks. By now, you may have realized MQTT is much more than just publish-subscribe. All the features discussed are just on the older MQTT 3.1.1 Version.

Stay Tuned for MQTT V5 Insights

![image](https://user-images.githubusercontent.com/56212392/172646150-38d6b00a-4460-4aaa-99d8-3c09e7a3ce6d.png)
