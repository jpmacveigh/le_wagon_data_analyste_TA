
<center><font style="color: red; font-size: 2em;"><strong>Skip the part above - Start reading below first!</strong></font></center>

<br>

Welcome to Kitt! 

The purpose of this challenge is to do a quick check if your machine is configured correctly.

We want to make sure it is properly connected to Kitt, so we can pick up your progress in the dashboard for specific challenges later in the bootcamp.


## Why?

Later in the bootcamp you will be writing code on your own machine, e.g. SQL code and dbt, Python and Machine Learning.

For those challenges we have a bunch of automated tests to check your code. When you made your changes, you will "push" them, and Kitt will pick up the result and show it on your dashboard.

At this point you should not worry about how this work, or what you will need to do later. We will show you when you need it.

For now you just need to execute a couple of quick commands to check your setup.


## Start the challenge

You have seen those strange commands at the top of the page. Now it is time to execute the first two.

👉 **Copy the commands** from the first lines **at the top of these instructions, above the red message**. You can copy the lines at once, but only this part:

```bash
# Create challenge folder
mkdir .......

# Download challenge
curl .......
```

So don't copy the last part that says `make`.

👉 **Open a terminal**

👉 **Paste the commands** you copied before, and hit `Enter`.

This will:
- create a folder for your challenge,
- download the challenge files for you,
- lett Kitt now you started this challenge.

In your terminal you should see this now:

```bash
x .gitignore/
x .lewagon/
x .lewagon/metadata.yml
x Makefile
x README.md
x autotest.sh
x tests/
x tests/__init__.py
x tests/test_demo.py
```


❌ If you see anything else, make a ticket with a TA!

You do not have to know what these files do. They just make things work. Don't change them.


## Create a file

Next, we'll create an empty file named `check`. This file will be the sign for Kitt that you passed this challenge.


👉 **Run this in your terminal** to create an empty file:

```bash
touch check
```

👉 Then run this in your terminal to **run the tests**:

```bash
make
```

You should get a longer output, with at the end a green line containing `1 passed`.

❌ If it doesn't contain `1 passed`, make a ticket with a TA!


## Pushing to Kitt

When `make` is 'happy' and all green, you should "push" your changes to GitHub!

Kitt will then pick it up, and show your challenge as completed.

👉 Copy-paste these commands into your terminal (you can run them all at once), and `Enter`:

```bash
git add check
git commit --message "Solved the first challenge of the bootcamp :)"
git push origin master
```

Shortly after your push is completed, [GitHub will tell Kitt](https://sebastien.saunier.me/blog/2014/04/21/practical-example-of-using-git-in-a-school.html) about this push thanks to a [webhook](https://developer.github.com/webhooks/). You'll learn what a webhook is later.

Kitt will then pull your code, run `make` and update your challenge completion. You should also see how your buddy of the day is doing!

Check your challenge on Kitt, you should see a green `100%` field now. Refresh the page if it doesn't.

❌ If after a minute, and a new refresh, you still don't see your process, make a ticket with a TA!


## ✅ Congratulations, your setup is working! 🏁

You can now leave the technical part behind and move to the next challenge.
