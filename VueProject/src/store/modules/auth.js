import Firebase from '../../api/firebase'

const state = {
    user: {
        loggedIn: false,
        displayName : '',
        email : '',
        emailVerified : false,
        photoURL : '',
        isAnonymous : true,
        uid : '',
        providerData : ''
    },
    error: {
        errorCode: '',
        errorMessage: ''
    }
};

const mutations = {
    AUTH_STATE_CHANGED (state, { user }) {
        state.user = user;
        if (user) { state.error = {
            errorCode: '',
            errorMessage: null
        } }
    },

    SET_USER (state, { key, val }) {
        Vue.set(state.user, key, val)
    },

    SET_ERROR (state, error) {
        state.error = error;
        state.user.loggedIn = false
    }
};

const actions = {
    onAuthStateChanged ({ commit }, user) {
        commit('AUTH_STATE_CHANGED', { user })
    },

    registerWithEmailAndPassword (state, user) {
        Firebase.registerWithEmailAndPassword(user)
    },

    signInWithEmailAndPassword (state, user) {
        Firebase.signInWithEmailAndPassword(user)
    },

    signInGoogle () {
        Firebase.signInGoogle()
    },

    signOut () {
        Firebase.signOut();
        sessionStorage.removeItem('userIdToken')
    }
};

const getters = {
    user: state => state.user,
    error: state => state.error,
    currentUserName: state => state.user.displayName,
    currentUserId: state => state.user.uid,
    currentUserEmail: state => state.user.email,
    getUserIdToken: state => state.user.userIdToken
};

export default {
    state,
    getters,
    actions,
    mutations
}

// export default {
//     namespaced: true,
//     state: {
//         user: {
//
//             loggedIn: false,
//             uid: '',
//             name: '',
//         },
//         error: '',
//         googleAuthProvider: googleAuthProvider,
//         facebookAuthProvider: facebookAuthProvider,
//         twitterAuthProvider: twitterAuthProvider,
//         githubAuthProvider: githubAuthProvider
//     },
//     mutations: {
//         logout(state) {
//             state.auth.signOut();
//         },
//         login(state, user) {
//             const promis = state.auth.signInWithEmailAndPassword(user.email, user.password);
//             promis.then((userResult) => {
//                 user.result(userResult);
//                 console.log("from Vuex : Done : " + user.email);
//             }).catch(error => {
//                 state.error = error.message;
//                 user.error(error)
//             })
//         },
//         signInGoogle(state, callBack) {
//             let provider = state.googleAuthProvider;
//             state.auth.signInWithPopup(provider).then((result) => {
//                 callBack.result(result)
//             }).catch((error) => {
//                 callBack.error(error)
//             });
//         },
//         signInFacebook(state, callBack) {
//             let provider = state.facebookAuthProvider;
//             state.auth.signInWithPopup(provider).then((result) => {
//                 callBack.result(result);
//             }).catch((error) => {
//                 callBack.error(error)
//             });
//         },
//         signInTwitter(state, callBack) {
//             let provider = state.twitterAuthProvider;
//             state.auth.signInWithPopup(provider).then((result) => {
//                 callBack.result(result);
//             }).catch((error) => {
//                 callBack.error(error)
//             });
//         },
//         signInGithub(state, callBack) {
//             let provider = state.githubAuthProvider;
//             state.auth.signInWithPopup(provider).then((result) => {
//                 callBack.result(result);
//             }).catch((error) => {
//                 callBack.error(error)
//             });
//         },
//         register(state, user) {
//             const promis = state.auth.createUserWithEmailAndPassword(user.email, user.password);
//             promis.then((userResult) => {
//                 console.log("from Vuex : Done : " + user.email);
//                 user.result(userResult)
//             }).catch(error => {
//                 state.error = error.message;
//                 user.error(error)
//             })
//         },
//         updateProfilePicture(state, image) {
//             state.auth.currentUser.updateProfile({
//                 photoURL: image.ref
//             }).then(() => {
//                 image.result()
//             }).catch(error => {
//                 image.error(error)
//             })
//         },
//         stateChanged(state, callBack) {
//             state.auth.onAuthStateChanged((user) => {
//                 if (user) {
//                     callBack.then(user)
//                 } else {
//                     callBack.catch()
//                 }
//             })
//         }
//     },
//     getters: {},
//     actions: {}
// }
