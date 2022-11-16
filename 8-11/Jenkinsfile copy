//write a pipline script thats
// run 4 stages 
// fetching   -> echo fetching 
// building   -> echo building 
// testing    -> echo testing 
// deploying  -> echo deploying 

//upload the file to a new repo in 
// your github using git commands 

pipeline{
    agent any
    stages{
        stage("fetching"){
            steps{
                echo "========fetching========"
            }
            
        }
        stage("building"){
            steps{
                echo "========building========"
            }
            
        }
        stage("testing"){
            steps{
                echo "========testing========"
            }
            
        }

        stage("deploying"){
            steps{
                echo "========deploying========"
            }
            
        }
        
    }
    post{
        always{
            echo "====++++always++++===="
        }
        success{
            echo "====++++only when successful++++===="
        }
        failure{
            echo "====++++only when failed++++===="
        }
    }

   
}

