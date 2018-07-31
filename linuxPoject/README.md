## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used

### And coding style tests

Explain what these tests test and why

```
Give an example
```


## Step-1 : Development Environment Information Details:-
* Public IP Address - 35.182.221.65
* Private Key - Can't be shared


## Step-2 :  uso da chave privada
* download da private key do amazon light sail
* copiar para a pasta ./ssh
* login via terminal 
* ssh -i ~/.ssh/LightsailDefaultPrivateKey-ca-central-1.pem ubuntu@35.182.221.65


## Step-3 : Create a new user named grader
* sudo adduser grader
* To check the User(grader) information :

sudo apt-get install finger
finger grader

## Step-4 : Give the grader the permission to sudo

## Step-3 : login grader
ssh grader@35.182.221.65 -p 2200 -i ~/.ssh/grader