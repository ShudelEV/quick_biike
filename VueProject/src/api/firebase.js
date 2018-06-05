import * as firebase from 'firebase/app'
import 'firebase/auth'

const conf = {
    apiKey: "AIzaSyCRuldqyfzhuUPeyYMhbPEDOpn6pN8Oo-0",
    authDomain: "quickbile2.firebaseapp.com",
    databaseURL: "https://quickbile2.firebaseio.com",
    projectId: "quickbile2",
    storageBucket: "quickbile2.appspot.com",
    messagingSenderId: "294614512032"
};

// initialize Firebase
firebase.initializeApp(conf);
var auth = firebase.auth();

// variable
var _userInfo = {};
var _error = {};

export default {

    // Sets up shortcuts to Firebase features and initiate firebase auth.

    initFirebase () {
        // Initiates Firebase auth and listen to auth state changes.
        auth.onAuthStateChanged(user => {
            if (user) { // User is signed in!
                // get token for backend auth
                user.getIdToken().then(idToken => { sessionStorage.userIdToken = idToken });
                // console.log(user);

                _userInfo = {
                    displayName: user.displayName,
                    email: user.email,
                    emailVerified: user.emailVerified,
                    photoURL: user.photoURL,
                    isAnonymous: user.isAnonymous,
                    uid: user.uid,
                    providerData: user.providerData
                };
                // _userInfo.loggedIn = _userInfo.emailVerified ? true : false;
                _userInfo.loggedIn = true;
                _App.$store.dispatch('onAuthStateChanged', _userInfo)
            } else {
                _userInfo = { loggedIn: false };
                _App.$store.dispatch('onAuthStateChanged', _userInfo)
            }
        })
    },

    getAuth () {
        return auth.currentUser || {}
    },

    // Signs-up
    registerWithEmailAndPassword (user) {
        auth.createUserWithEmailAndPassword(user.email, user.password)
            .then(function (result) {
                user.result()
            })
            .catch(function(error) {
                _error = {
                    errorCode : error.code,
                    errorMessage : error.message
                };
                _App.$store.commit('SET_ERROR', _error);
                // if (_error.errorCode === 'auth/weak-password') {
                //     alert('The password is too weak!');
                // } else {
                //     alert(_error.errorMessage);
                // }
                console.log(error);
                })
    },

    sendEmailVerification () {
        auth.currentUser.sendEmailVerification().then(function() {
            // Email Verification sent!
            alert('Email Verification Sent!');
        });
    },

    // Signs-in
    signInWithEmailAndPassword (user) {
        auth.signInWithEmailAndPassword(user.email, user.password)
            .then(function (result) {
                user.result()
            })
            .catch(function(error) {
                _error = {
                    errorCode : error.code,
                    errorMessage : error.message
                };
                _App.$store.commit('SET_ERROR', _error);
                // if (_error.errorCode === 'auth/wrong-password') {
                //     alert('Wrong password!');
                // } else {
                //     alert(_error.errorMessage);
                // }
                console.log(error);
            })
    },

    signInGoogle () {
        // Sign in Firebase using popup auth and Google as the identity provider.
        var provider = new firebase.auth.GoogleAuthProvider();
        auth.signInWithPopup(provider).catch(function(error) {
            _error = {
                errorCode : error.code,
                errorMessage : error.message,
                // The email of the user's account used.
                email : error.email,
                // The firebase.auth.AuthCredential type that was used.
                credential : error.credential,
            };
            _App.$store.commit('SET_ERROR', _error);
            if (error.code === 'auth/account-exists-with-different-credential') {
              alert('You have already signed up with a different auth provider for that email.');
              // If you are using multiple auth providers on your app you should handle linking
              // the user's accounts here.
            } else {
                console.error(error);
            }
        });
    },

    // Signs-out
    signOut () {
        // Sign out of Firebase.
        auth.signOut()
    }
}
