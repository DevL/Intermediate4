# Pair- and mob programming

Perhaps the single best way of working with code is to do it together. This however is an often unpracticed skill that takes some discipline to get the most out it. When working together, either as a pair or in a group (mob), there are two primary roles that people play.

1. The **driver** acts as an intelligent input device.
* Avoid performing actions without a navigator having expressed an intent.

2. The **navigator** or **navigators** instruct the driver what to do.
* The instructions should be at a as high level as possible.
  * This will vary depending who is driving and who is navigating. Adapt accordingly. 
  * It is better to express "map over the items and apply a function to each of them that does X" rather than "type 'i-t-e-m' followed by 'dot'..."
    * You _may_ have to dive down to a lower level of instructions from time to time, but be quick to move back up again.

Now for the tricky part that people often forget: rotate roles frequently! The driver becomes a navigator and a navigator becomes the driver. You can for example rotate "on the clock" as in rotating every 5-15 minutes.

## Resources

* Martin Fowler's [_On Pair Programming_](https://martinfowler.com/articles/on-pair-programming.html).
* A [short video in Swedish](https://www.youtube.com/watch?v=vJ_QotHDAXc) about strong pairing.
