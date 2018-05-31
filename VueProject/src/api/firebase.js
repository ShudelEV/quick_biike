import firebase from 'firebase'

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
var _userRef = null;

export default {

    // Sets up shortcuts to Firebase features and initiate firebase auth.

    initFirebase () {
        // Initiates Firebase auth and listen to auth state changes.
        auth.onAuthStateChanged(this.onAuthStateChanged.bind(this))
    },

    getAuth () {
        return auth.currentUser || {}
    },

    // Signs-in
    signInGoogle () {
        // Sign in Firebase using popup auth and Google as the identity provider.
        var provider = new firebase.auth.GoogleAuthProvider();
        auth.signInWithPopup(provider)
    },

    // Signs-out
    signOut () {
        // Sign out of Firebase.
        auth.signOut()
    },

    // Triggers when the auth state change for instance when the user signs-in or signs-out.
    onAuthStateChanged (user) {
        if (user) { // User is signed in!
            this.fetchUserInfo(user.uid)
                .then(val => {
                    _userInfo = {
                        loggedIn: true,
                        uid: user.uid,
                        name: val.name || user.displayName,
                        profilePicUrl: user.photoURL
                    };
                    _App.$store.dispatch('onAuthStateChanged', Object.assign({}, _userInfo))
                }).catch(() => {
                    _userInfo = {
                        loggedIn: true,
                        uid: user.uid,
                        name: user.displayName,
                        profilePicUrl: user.photoURL
                    };
                    _App.$store.dispatch('onAuthStateChanged', Object.assign({}, _userInfo))
                })
        } else {
            _userInfo = {
                loggedIn: false,
                uid: '',
                name: 'guest',
                profilePicUrl: ''
            };
            _App.$store.dispatch('onAuthStateChanged', Object.assign({}, _userInfo))
        }
    },

    fetchUserInfo (uid) {
        return new Promise((resolve, reject) => {
            _userRef = database.ref('users');
            _userRef.child(uid).once('value')
                .then(snapshot => {
                      const user = snapshot.val();
                      resolve(user)
                }).catch(reject)
        })
    },

    setUserInfo (key, val) {
        return new Promise((resolve, reject) => {
            if (key && val && this.checkSignedInWithMessage()) {
                _userRef = database.ref('users').child(_userInfo.uid).child(key);
                _userRef.set(val)
                    .then(() => {
                        _userInfo[key] = val;
                        resolve()
                    }).catch(reject)
            }
        })
    },

    checkSignedInWithMessage () {
        return auth.currentUser ? true : false
    }
}
