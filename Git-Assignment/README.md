# task-1 Basic Staging, Committing, and Pushing
- Create a new folder: 
``` mkdir my-git-task && cd my-git-task``` 

- Initialize Git & Create files:

```
git init

touch Code.txt Log.txt Output.txt
```

- Stage Code.txt and Output.txt:
```git add Code.txt Output.txt```

- Commit them:
```git commit -m "Add Code and Output files"```

- Push to GitHub:
```
git remote add origin <your-github-repo-url>
git branch -M main
git push -u origin main
```
